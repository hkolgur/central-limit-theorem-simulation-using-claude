"""Visualization tools for Central Limit Theorem Simulator."""

from pathlib import Path
from typing import Optional

import matplotlib.pyplot as plt
import numpy as np
from numpy.typing import NDArray


class CLTVisualizer:
    """Create visualizations of Central Limit Theorem simulations."""

    def __init__(self, figsize: tuple[int, int] = (14, 10)):
        """Initialize the visualizer.

        Args:
            figsize: Figure size (width, height) in inches.
        """
        self.figsize = figsize

    def plot_distribution_comparison(
        self,
        means: NDArray[np.floating],
        distribution_name: str,
        output_path: Optional[Path] = None,
    ) -> None:
        """Create visualization comparing sample means to normal distribution.

        Args:
            means: Array of sample means from simulation.
            distribution_name: Name of the distribution used.
            output_path: Optional path to save the figure.
        """
        fig, axes = plt.subplots(1, 2, figsize=self.figsize)

        # Histogram with normal curve overlay
        ax1 = axes[0]
        ax1.hist(means, bins=30, density=True, alpha=0.7, color='skyblue', edgecolor='black')

        # Overlay normal distribution
        mu, sigma = means.mean(), means.std()
        x = np.linspace(means.min(), means.max(), 100)
        ax1.plot(x, 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((x - mu) / sigma) ** 2),
                 'r-', linewidth=2, label='Normal Distribution')

        ax1.set_xlabel('Sample Mean', fontsize=12, fontweight='bold')
        ax1.set_ylabel('Density', fontsize=12, fontweight='bold')
        ax1.set_title(f'{distribution_name}\nHistogram of Sample Means', fontsize=13, fontweight='bold')
        ax1.legend()
        ax1.grid(True, alpha=0.3)

        # Q-Q Plot for normality assessment
        ax2 = axes[1]
        sorted_means = np.sort(means)
        theoretical_quantiles = np.sort(np.random.standard_normal(len(means)))
        ax2.scatter(theoretical_quantiles, sorted_means, alpha=0.6, s=30)

        # Add reference line
        min_val = min(theoretical_quantiles.min(), sorted_means.min())
        max_val = max(theoretical_quantiles.max(), sorted_means.max())
        ax2.plot([min_val, max_val], [min_val, max_val], 'r--', linewidth=2, label='Perfect Normal')

        ax2.set_xlabel('Theoretical Quantiles', fontsize=12, fontweight='bold')
        ax2.set_ylabel('Sample Quantiles', fontsize=12, fontweight='bold')
        ax2.set_title(f'{distribution_name}\nQ-Q Plot', fontsize=13, fontweight='bold')
        ax2.legend()
        ax2.grid(True, alpha=0.3)

        fig.suptitle(f'Central Limit Theorem: {distribution_name}',
                     fontsize=15, fontweight='bold', y=1.00)
        plt.tight_layout()

        if output_path:
            plt.savefig(output_path, dpi=300, bbox_inches='tight')
            print(f"✅ Plot saved to: {output_path}")

        plt.show()

    def plot_convergence(
        self,
        means: NDArray[np.floating],
        distribution_name: str,
        output_path: Optional[Path] = None,
    ) -> None:
        """Plot convergence of sample means to theoretical mean.

        Args:
            means: Array of sample means from simulation.
            distribution_name: Name of the distribution used.
            output_path: Optional path to save the figure.
        """
        fig, axes = plt.subplots(2, 1, figsize=self.figsize)

        # Running mean
        ax1 = axes[0]
        running_mean = np.cumsum(means) / np.arange(1, len(means) + 1)
        ax1.plot(running_mean, linewidth=2, color='steelblue', label='Running Mean')
        ax1.axhline(y=means.mean(), color='r', linestyle='--', linewidth=2, label=f'Final Mean: {means.mean():.4f}')
        ax1.set_ylabel('Mean Value', fontsize=12, fontweight='bold')
        ax1.set_title(f'{distribution_name}\nConvergence of Sample Means (Law of Large Numbers)',
                     fontsize=13, fontweight='bold')
        ax1.legend()
        ax1.grid(True, alpha=0.3)

        # Running standard deviation
        ax2 = axes[1]
        running_std = np.array([np.std(means[:i+1]) for i in range(len(means))])
        ax2.plot(running_std, linewidth=2, color='coral', label='Running Std Dev')
        ax2.axhline(y=means.std(), color='r', linestyle='--', linewidth=2,
                   label=f'Final Std Dev: {means.std():.4f}')
        ax2.set_xlabel('Number of Samples', fontsize=12, fontweight='bold')
        ax2.set_ylabel('Standard Deviation', fontsize=12, fontweight='bold')
        ax2.set_title(f'{distribution_name}\nConvergence of Sample Std Dev',
                     fontsize=13, fontweight='bold')
        ax2.legend()
        ax2.grid(True, alpha=0.3)

        fig.suptitle(f'Central Limit Theorem Convergence: {distribution_name}',
                     fontsize=15, fontweight='bold', y=0.995)
        plt.tight_layout()

        if output_path:
            plt.savefig(output_path, dpi=300, bbox_inches='tight')
            print(f"✅ Plot saved to: {output_path}")

        plt.show()

    def plot_multiple_distributions(
        self,
        results: dict[str, NDArray[np.floating]],
        output_path: Optional[Path] = None,
    ) -> None:
        """Compare multiple distributions side by side.

        Args:
            results: Dictionary mapping distribution names to sample means arrays.
            output_path: Optional path to save the figure.
        """
        n_dists = len(results)
        fig, axes = plt.subplots(1, n_dists, figsize=(6*n_dists, 5))

        if n_dists == 1:
            axes = [axes]

        for ax, (dist_name, means) in zip(axes, results.items()):
            ax.hist(means, bins=30, density=True, alpha=0.7, color='skyblue', edgecolor='black')

            # Overlay normal distribution
            mu, sigma = means.mean(), means.std()
            x = np.linspace(means.min(), means.max(), 100)
            ax.plot(x, 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((x - mu) / sigma) ** 2),
                   'r-', linewidth=2)

            ax.set_xlabel('Sample Mean', fontsize=11, fontweight='bold')
            ax.set_ylabel('Density', fontsize=11, fontweight='bold')
            ax.set_title(f'{dist_name}\n(μ={mu:.4f}, σ={sigma:.4f})', fontsize=12, fontweight='bold')
            ax.grid(True, alpha=0.3)

        fig.suptitle('Central Limit Theorem: Comparison of Distributions',
                     fontsize=15, fontweight='bold', y=1.00)
        plt.tight_layout()

        if output_path:
            plt.savefig(output_path, dpi=300, bbox_inches='tight')
            print(f"✅ Plot saved to: {output_path}")

        plt.show()
