import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DIL",  # Replace with your own username
    version="0.0.1",
    author="DIL-Project",
    author_email="lrtk@kakao.com",
    description="가명처리 기술을 손 쉽게 사용할 수 있는 라이브러리",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LRTK-CODER/DIL-Project",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)
