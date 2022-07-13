{
  description = "A basic flake with a shell";
  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
  inputs.flake-utils.url = "github:numtide/flake-utils";

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system: let
      pkgs = nixpkgs.legacyPackages.${system};
    in {
      devShell = pkgs.mkShell {
			  nativeBuildInputs = with pkgs; [ 

			  python3 
			  python39Packages.youtube-dl 
              python39Packages.pytube 
              python39Packages.setuptools
              python39Packages.build
              ffmpeg

              ];

        buildInputs = [ ];
      };
    });
}
