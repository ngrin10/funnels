#!/usr/bin/env python3
"""Check a public skill package. Uses Python 3.9+ and no extra libraries."""
import argparse
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
GUIDES = (
    'interview', 'context-template', 'spec-template', 'builder-template',
    'checkpoint-template', 'prompt-template', 'handoff-template',
    'conversion-checks', 'copy', 'screens', 'build', 'measurement',
    'limits', 'research', 'offer-brief', 'evidence', 'writing', 'coverage',
    'plain-terms', 'post-purchase',
)
PLAYS = (
    'offers', 'low-ticket-ascension', 'call-funnels', 'sales-videos', 'ads-to-page',
    'positioning', 'ecom', 'consumer-apps', 'retention', 'health-offers',
)
SURFACES = ('pages', 'signup', 'forms', 'popups', 'paywalls', 'onboarding')
REQUIRED = ['SKILL.md', 'README.md', 'LICENSE', 'scripts/validate.py'] + [
    f'references/{name}.md' for name in GUIDES
] + [f'references/surfaces/{name}.md' for name in SURFACES] + [
    'references/data-template.json', 'examples/booking-page.md',
    'examples/review-cases.md', 'examples/limits-in-action.md',
    'references/plays.md',
] + [f'references/plays/{name}.md' for name in PLAYS]
SECTIONS = {
    'references/context-template.md': ['Limits and help needed', 'Inputs', 'Field list', 'Path today', 'Decisions and conflicts', 'Outputs and inputs', 'Rules'],
    'references/spec-template.md': ['Checkpoint', 'Limits and skills', 'Data rules', 'Inputs and evidence', 'Goal and success measure', 'Outputs and inputs', 'Events', 'Test plan', 'Open items', 'Approval and readiness', 'Review log'],
    'references/builder-template.md': ['Product and path', 'Inputs and decisions', 'Data rules', 'Changes to build', 'Shared work and order', 'Open items and next action', 'Review'],
    'references/prompt-template.md': ['1. CONTEXT', '2. SPEC', '3. ROLLOUT AND TEST', '4. EVENTS', '5. QUESTIONS BEFORE BUILDING', '6. HOW TO WORK'],
}
# Extra private terms can be supplied from a private file outside the repo.
PATTERNS = {
    'local user path': r'/Users/[^\s]+',
    'private document host': r'https?://[^\s]*(?:notion\.(?:so|site)|slack\.com|figma\.com)',
    'UUID': r'\b[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}\b',
    'secret-like value': r'\b(?:sk-[A-Za-z0-9_-]{16,}|gh[pousr]_[A-Za-z0-9]{20,})\b',
}


def check(private_terms=None):
    errors = []
    for name in REQUIRED:
        if not (ROOT / name).is_file():
            errors.append(f'Missing file: {name}')
    public = [p for p in ROOT.rglob('*') if '.git' not in p.relative_to(ROOT).parts and p.is_file()]
    contents = {}
    for path in public:
        if path.is_symlink():
            errors.append(f'Symlink must not be packaged: {path.relative_to(ROOT)}')
            continue
        try:
            contents[path] = path.read_text()
        except (UnicodeError, OSError):
            errors.append(f'Unexpected unreadable or binary file: {path.relative_to(ROOT)}')
    skill = contents.get(ROOT / 'SKILL.md', '')
    front = re.match(r'^---\n(.*?)\n---\n', skill, re.S)
    if not front:
        errors.append('Missing frontmatter')
    else:
        for field in ('name', 'description'):
            if not re.search(rf'^{field}:\s*\S', front[1], re.M):
                errors.append(f'Missing frontmatter field: {field}')
    stages = re.findall(r'^## ([1-8])\. ', skill, re.M)
    if stages != [str(i) for i in range(1, 9)]:
        errors.append('Core must keep the eight stages in order')
    for name, sections in SECTIONS.items():
        content = contents.get(ROOT / name, '')
        for section in sections:
            if section not in content:
                errors.append(f'{name}: missing section {section}')
    for name in ('SKILL.md', 'references/context-template.md'):
        if 'NEEDS SKILL' not in contents.get(ROOT / name, ''):
            errors.append(f'{name}: missing explicit skill-gap state')
    for name in ('SKILL.md', 'references/prompt-template.md', 'references/writing.md'):
        if 'fifth-grade' not in contents.get(ROOT / name, ''):
            errors.append(f'{name}: missing plain-language rule')
    terms = []
    if private_terms:
        terms_path = Path(private_terms).resolve()
        if terms_path.is_relative_to(ROOT):
            errors.append('Private terms must stay outside the public package')
        else:
            try:
                terms = [s.strip() for s in terms_path.read_text().splitlines() if s.strip()]
            except OSError:
                errors.append('Could not read the private terms file')
    for path, content in contents.items():
        # The validator contains the generic patterns themselves. Extra terms
        # below still check every file, including this script.
        if path != Path(__file__).resolve():
            for label, pattern in PATTERNS.items():
                if re.search(pattern, content, re.I):
                    errors.append(f'{path.relative_to(ROOT)}: possible {label}; review before publishing')
        if any(re.search(r'(?<!\w)' + re.escape(term) + r'(?!\w)', content, re.I) for term in terms):
            errors.append(f'{path.relative_to(ROOT)}: private term found; value withheld')
        if path.suffix == '.md':
            for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)', content):
                if re.match(r'^[a-z]+://|^#', link):
                    continue
                target = (path.parent / link.split('#')[0]).resolve()
                if not target.is_relative_to(ROOT) or not target.exists():
                    errors.append(f'{path.relative_to(ROOT)}: invalid local link {link}')
    try:
        data = json.loads(contents.get(ROOT / 'references/data-template.json', ''))
        for field in ('what', 'pulled', 'source', 'account', 'window', 'group_rules', 'count_unit', 'metric', 'numerator', 'denominator', 'value', 'unit', 'label', 'limits', 'privacy'):
            if field not in data:
                errors.append(f'Data template missing field: {field}')
        if data.get('value') is not None or data.get('label') != 'NOT KNOWN':
            errors.append('Unfilled data template must not look like a real result')
    except (ValueError, TypeError):
        errors.append('Invalid data template JSON')
    if errors:
        print('\n'.join(errors))
        return 1
    print(f'PASS: {len(REQUIRED)} required files; links, metadata, eight stages, templates, data fields, plain-language/skill-gap rules, and privacy patterns.')
    print('These are package checks. They do not prove interview quality or catch every private detail.')
    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--private-terms', help='Private file outside this repo, one term per line; values are never printed')
    sys.exit(check(parser.parse_args().private_terms))
