{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "leapyear.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyMOWltxrLmGRjNIVx/Xmmu1",
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
        "<a href=\"https://colab.research.google.com/github/ruveydee/GitHubTest/blob/master/leapyear.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kp16V2CcjkpH",
        "outputId": "6d39fe9c-31f4-4dbe-90cb-a1be9c221b20"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a year please: 2012\n",
            "True\n"
          ]
        }
      ],
      "source": [
        "x= int(input(\"Enter a year please: \"))\n",
        "\n",
        "leap = (x % 4 == 0) and ((x % 100 != 0) or (x % 400 == 0))\n",
        "\n",
        "print(leap)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "T5mMSV-akKWC"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}