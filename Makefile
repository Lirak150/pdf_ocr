build_image:
	@docker build -t pdf_ocr .

run:
	@docker run --rm -it --mount type=bind,src="$$(pwd)/ocr_files",dst=/ocr_files pdf_ocr