{ pkgs }:
pkgs.mkShell {
  buildInputs = [
    pkgs.python39Full
    pkgs.python39Packages.fastapi
    pkgs.python39Packages.uvicorn
    pkgs.python39Packages.jinja2
    pkgs.qemu
  ];
}