# Contributing

## Local validation

```bash
bash install/doctor.sh --capability docs
python3 shared/scripts/stage-gate.py --request-dir examples/project-management-pm-recheck --stage all
python3 scripts/readme-gate.py --readme README.md
python3 scripts/readme-gate.py --readme docs/README_en.md
```

## Pull request checklist

- Update examples and gates together with template changes.
- Add minimal reproduction input for parser changes.
- Keep real prototypes, screenshots, logs, and `.env` files untracked.
- Preserve parent, child, and grandchild data relationships.
- Keep Chinese and English README structures aligned.
- Confirm all README images are registered in `assets/asset-manifest.json`.
