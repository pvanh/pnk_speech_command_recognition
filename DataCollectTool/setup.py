import setuptools

setuptools.setup(
    name="data_collect_tool",
    version="1.0.3",
    entry_points={
      'gui_scripts': [
          'data-collect-tool = DataCollectTool.__main__:main'
      ]
    },
    author="Nguyen Minh Hieu",
    author_email="nguyenminhhieu.it1.k52@gmail.com",
    description="Data Collect Tool",
    long_description="A tool to collect speech command data",
    long_description_content_type="text/markdown",
    url="https://github.com/Artori-kun/SpeechCommandDataCollectingTool",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

