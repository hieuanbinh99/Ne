from setuptools import setup, find_packages

setup(
    name="ne-agent",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "openai>=1.0.0",
        "python-dotenv>=1.0.0",
        "pyyaml>=6.0",
        "requests>=2.28.0",
    ],
    entry_points={
        "console_scripts": [
            "ne-agent=ne_agent.main:main",
        ],
    },
)
