# MarianNMT Translation Demo

This repository provides a simple Python application demonstrating the use of MarianNMT for machine translation, specifically translating text from English to Spanish using the Hugging Face `transformers` library.

## Introduction

MarianNMT is an efficient neural machine translation framework developed by the Microsoft Translator team, focusing on speed and efficiency for both training and inference. This demo utilizes MarianNMT through the `transformers` library to showcase an end-to-end translation process, including necessary steps to set up a compatible environment.

## Installation

### Prerequisites

- Python 3.8
- Conda environment
- NVIDIA GPU (optional for GPU acceleration)

### Setting Up Environment

1. **Install Anaconda or Miniconda**: Follow the instructions on the [official website](https://docs.conda.io/en/latest/miniconda.html) to install Miniconda.

2. **Create and Activate Conda Environment**:
   ```bash
   conda create --name marian-nmt python=3.8
   conda activate marian-nmt
   ```

3. **Install Dependencies**:
   Ensure you are in the `marian-nmt` environment and run:
   ```bash
   conda install pytorch torchvision torchaudio cudatoolkit=12.1 -c pytorch
   pip install transformers
   conda install -c conda-forge sentencepiece
   ```

## Usage

To translate text using the provided script, ensure your environment is activated and run:

```bash
python translate.py
```

The `translate.py` script loads a pre-trained MarianNMT model to translate English text to Spanish. You can modify the script to translate different texts or to use other language pairs supported by MarianNMT models.

## Contributing

Contributions to improve the demo or extend its functionality are welcome. Please feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is open-sourced under the MIT License. See the LICENSE file for more details.

## Acknowledgements

- Thanks to the Hugging Face team for the `transformers` library.
- Thanks to the MarianNMT team for their work on the translation framework.