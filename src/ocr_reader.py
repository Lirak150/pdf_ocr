import subprocess


class OCRReader:
    def __init__(self, input_filepath: str, output_filepath: str):
        self._input_filepath = input_filepath
        self._output_filepath = output_filepath

    def ocr_file(self) -> tuple[int, str]:
        popen = subprocess.Popen(
            f"ocrmypdf -l rus --sidecar {self._output_filepath} --output-type=none {self._input_filepath} -",
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE,
        )
        stdout_orig, stderr_orig = popen.communicate()
        return_code = popen.returncode
        stdout = stdout_orig.decode("utf-8", errors="ignore").replace("\r", "")
        stderr = stderr_orig.decode("utf-8", errors="ignore").replace("\r", "")
        if return_code == 0:
            return 0, stdout
        else:
            return 1, stderr
