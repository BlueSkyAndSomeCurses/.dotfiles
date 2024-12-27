{
  description = "BlueSkyAndSomeCurses Nix config flake";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";

    home-manager = {
      url = "github:nix-community/home-manager";
      inputs.nixpkgs.follows = "nixpkgs";
    };

    nix-darwin.url = "github:LnL7/nix-darwin";
    nix-darwin.inputs.nixpkgs.follows = "nixpkgs";
    nix-homebrew.url = "github:zhaofengli-wip/nix-homebrew";
  };

  outputs = { self, nixpkgs, nix-darwin, nix-homebrew, ... }@inputs:
    let
      darwin-configuration = { ... }: {
        system.configurationRevision = self.rev or self.dirtyRev or null;
      };
    in {
      nixosConfigurations.default = nixpkgs.lib.nixosSystem {
        specialArgs = { inherit inputs; };
        modules = [
          ./host/default/configuration.nix
          inputs.home-manager.nixosModules.default
        ];
      };

      darwinConfigurations."darwin" = nix-darwin.lib.darwinSystem {
        specialArgs = { inherit inputs; };
        modules = [
          darwin-configuration
          ./host/darwin/configuration.nix
          nix-homebrew.darwinModules.nix-homebrew
          {
            nix-homebrew = {
              # Install Homebrew under the default prefix
              enable = true;

              # Apple Silicon Only: Also install Homebrew under the default Intel prefix for Rosetta 2
              enableRosetta = true;

              # User owning the Homebrew prefix
              user = "vitya";
              # mutableTaps = false;
            };
          }
          inputs.home-manager.darwinModules.home-manager
        ];
      };

      darwinPackages = self.darwinConfiguration."darwin".pkgs;

    };
}
