with import <nixpkgs { };
python3Packages.buildPythonPackage { 
	pname = "ytmpbash";
	version = "0.1";

	src = ./.;
	
	propagatedBuildInputs = python3Packages; {
		sys
		re
		os
		youtube_dl
		subprocess
		getpass
	};
	checkInputs = {
		pytest
		mock
	};
	doCheck = false;
	checkPhase = ''
		pytest
	'';
	pythonImportsCheck = [ ./. ];
}
