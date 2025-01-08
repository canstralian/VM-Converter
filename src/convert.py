import subprocess

def convert_image(input_path, output_path, input_format, output_format):
    try:
        subprocess.run([
            'qemu-img', 'convert', '-f', input_format, '-O', output_format,
            input_path, output_path
        ], check=True)
        return True, output_path
    except subprocess.CalledProcessError as e:
        return False, str(e)