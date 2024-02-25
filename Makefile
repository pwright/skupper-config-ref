
.PHONY: process-%
process-%:
	cd $*-reference; skupper man --platform $*
	# rm -rf $*-reference/docs.out/*
	sed -i '/.*spf13.*/d' $*-reference/docs.out/*.md
