{
  outputs = { self, nixpkgs, flake-utils, mach-nix }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };

        mach-nix-lib = import mach-nix {
          inherit pkgs;
          python = "python310";
        };

        ytmp = mach-nix-lib.buildPythonPackage ./.;
      in {
        packages = { inherit ytmp; };
        defaultPackage = ytmp;

        devShell = pkgs.mkShell {
          inputsFrom = builtins.attrValues self.packages.${system};
          buildInputs = with pkgs; [
            mypy
            black
            python310Packages.pytest
            python310Packages.pytestcov
          ];
        };
      });
}
