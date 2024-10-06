.PHONY: dependencies
dependencies:
	git submodule update --init --recursive --remote

.PHONY: serve
serve:
	hugo server --buildDrafts --disableFastRender

.PHONY: site
site:
	- rm -rf public/
	hugo

.PHONY: formatting
formatting:
	- $(CONDA) markdownlint-cli2 "content/**/*.{md,markdown}" --fix --config .markdownlint.yaml
