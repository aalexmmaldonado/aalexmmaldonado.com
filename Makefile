.PHONY: dependencies
dependencies:
	git submodule update --init --recursive

.PHONY: serve
serve:
	hugo server --disableFastRender
