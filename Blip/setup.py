import setuptools

setuptools.setup(
    name="blip",
    version="PACKAGE_VERSION",
    description="Python package to intercept all external api call during django test.",
    long_description="TEST",
    long_description_content_type="text/markdown",
    author="yale",
    author_email="yalefresne@gmail.com",
    license="MIT License",
    package_dir={"": "src"},
    packages=setuptools.find_namespace_packages(where="src"),
    zip_safe=False,
    url="https://github.com/yalefresne/blip/",
    install_requires=["httpretty>=1.1.4"],
    python_requires=">=3.9",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
