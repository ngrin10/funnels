#!/usr/bin/env python3
"""Check the public skill package using only Python's standard library."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ['SKILL.md', 'README.md', 'LICENSE'] + [
    f'references/{name}.md' for name in (
        'interview', 'context-template', 'spec-template', 'prompt-template',
        'handoff-template', 'conversion-checks', 'copy', 'screens', 'build',
        'measurement')
] + ['examples/booking-page.md', 'examples/review-cases.md']
SECTIONS = {
    'references/context-template.md': ['Inputs', 'Field list', 'Path today', 'Decisions and conflicts', 'Rules'],
    'references/spec-template.md': ['Checkpoint', 'Inputs and evidence', 'Goal and success measure', 'Events', 'Test plan', 'Open items', 'Approval and readiness', 'Review log'],
    'references/prompt-template.md': ['1. CONTEXT', '2. SPEC', '3. ROLLOUT AND TEST', '4. EVENTS', '5. QUESTIONS BEFORE BUILDING', '6. HOW TO WORK'],
}
# These catch common accidental disclosures, not all confidential information.
PRIVATE = {
    'local user path': r'/Users/[^\s]+',
    'private document host': r'https?://[^\s]*(?:notion\.(?:so|site)|slack\.com|figma\.com)',
    'UUID': r'\b[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}\b',
    'secret-like value': r'\b(?:sk-[A-Za-z0-9_-]{16,}|gh[pousr]_[A-Za-z0-9]{20,})\b',
}

def check():
    errors = []
    for name in REQUIRED:
        if not (ROOT / name).is_file():
            errors.append(f'Missing file: {name}')
    skill = (ROOT / 'SKILL.md').read_text() if (ROOT / 'SKILL.md').exists() else ''
    front = re.match(r'^---\n(.*?)\n---\n', skill, re.S)
    if not front:
        errors.append('Missing frontmatter')
    else:
        for field in ('name', 'description'):
            if not re.search(rf'^{field}:\s*\S', front[1], re.M):
                errors.append(f'Missing frontmatter field: {field}')
    for name, sections in SECTIONS.items():
        content = (ROOT / name).read_text() if (ROOT / name).exists() else ''
        for section in sections:
            if section not in content:
                errors.append(f'{name}: missing section {section}')
    markdown = list(ROOT.rglob('*.md'))
    public_files = [p for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.parts]
    for path in public_files:
        if path.suffix == '.py':
            continue  # Rules are code, so pattern text is not evidence of a disclosure.
        content = path.read_text()
        for label, pattern in PRIVATE.items():
            if re.search(pattern, content):
                errors.append(f'{path.relative_to(ROOT)}: possible {label}; review before publishing')
    for path in markdown:
        if '.git' in path.parts:
            continue
        content = path.read_text()
        for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)', content):
            if re.match(r'^[a-z]+://|^#', link):
                continue
            target = (path.parent / link.split('#')[0]).resolve()
            if not target.is_relative_to(ROOT) or not target.exists():
                errors.append(f'{path.relative_to(ROOT)}: invalid local link {link}')
    if errors:
        print('\n'.join(errors))
        return 1
    print(f'PASS: {len(REQUIRED)} required files, frontmatter, sections, local links, and privacy patterns ({len(markdown)} Markdown files).')
    print('Manual content review and live interview trials are still needed.')
    return 0

if __name__ == '__main__':
    sys.exit(check())
