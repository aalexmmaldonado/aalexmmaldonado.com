.PHONY: dependencies
dependencies:
	git submodule update --init --recursive --remote

.PHONY: serve
serve:
	hugo server --buildDrafts --disableFastRender
