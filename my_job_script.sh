!/bin/bash
SBATCH --time=03:00:00
SBATCH --nodes=1
SBATCH --cpus-per-task=7
SBATCH --mem-per-cpu=32G
SBATCH --account=def-gevrynic
SBATCH --job-name=pycenic_test1
SBATCH --output=%x-%j.out