{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOYgk7ApUyRWo2EdGpDVxHN",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/keden49/python-freecodecamp/blob/main/Test.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "gqJfyc_brSts"
      },
      "outputs": [],
      "source": [
        "def caesar(text, shift, encrypt=True):\n",
        "\n",
        "    if not isinstance(shift, int):\n",
        "        return 'Shift must be an integer value.'\n",
        "\n",
        "    if shift < 1 or shift > 25:\n",
        "        return 'Shift must be an integer between 1 and 25.'\n",
        "\n",
        "    alphabet = 'abcdefghijklmnopqrstuvwxyz'\n",
        "\n",
        "    if not encrypt:\n",
        "        shift = -shift\n",
        "\n",
        "    shifted_alphabet = alphabet[shift:] + alphabet[:shift]\n",
        "\n",
        "    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())\n",
        "\n",
        "    encrypted_text = text.translate(translation_table)\n",
        "\n",
        "    return encrypted_text\n",
        "\n",
        "def encrypt(text, shift):\n",
        "    return caesar(text, shift)\n",
        "\n",
        "def decrypt(text, shift):\n",
        "    return caesar(text, shift, encrypt=False)\n",
        "\n"
      ]
    }
  ]
}