# Import U
import uppaal_random_generator.version as version

# Import S
import setuptools

with open('requirements.txt') as fp:
    install_requires = fp.read().encode("utf-8")

with open("README.md", "r") as fh:
    long_description = fh.read().encode("utf-8")

setuptools.setup(
    name="uppaal_random_generator",
    packages=["uppaal_random_generator"],
    version=version.VERSION,
    author="Tim Lucas Sabelmann",
    author_email="tim.sabelmann@hotmail.de",
    description="Uppaal random model generator including a CLI tool.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tsabelmann/uppaal_random_generator",
    python_requires=">=3.8",
    install_requires=install_requires,
    py_modules=[
        'main'
    ],
    entry_points={
        "console_scripts": [
            "uppaal-random-generator = main:main",
            "uppaal_random_generator = main:main"
        ]
    }
)
