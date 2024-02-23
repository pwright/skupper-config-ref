
.PHONY: process-%
process-%:
	cd $*-reference; skupper man 
	rm -rf $*-reference/docs.out/*.1
	sed -i '/.*spf13.*/d' $*-reference/docs.out/*.md
