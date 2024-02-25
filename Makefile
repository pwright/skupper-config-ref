
.PHONY: process-%
process-%:
	cd $*-reference; skupper man --platform $*
	
	sed -i '/.*spf13.*/d' $*-reference/docs.out/*.md
	rm $*-reference/docs.out/*.1