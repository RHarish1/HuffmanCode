# HuffmanCode
Compress and decompress File 

![GitHub](https://img.shields.io/github/license/RHarish1/HuffmanCode)

## Description

This is a Python implementation of the Huffman coding algorithm, a widely used compression technique in computer science. Huffman coding is used to encode data in a way that reduces its size, making it useful for data compression and transmission.

Several data structures are being used in this implementation:

BinaryTreeNode: This class represents a node in the binary tree that is constructed during the Huffman coding process. It contains attributes for the character value, frequency, and references to the left and right child nodes.

Heap: A heap is used to maintain the frequency of characters in ascending order. Python's heapq module is used to create a min-heap. The heap is used to efficiently select nodes with the lowest frequencies during the tree construction.

Dictionary: Dictionaries are used to store frequency information for characters. The keys are characters, and the values are their corresponding frequencies.

Strings: Strings are used to represent the encoded bits for characters. The __codes dictionary stores the Huffman codes for each character, and the __reversecodes dictionary stores the reverse mapping of codes to characters.

Lists (Arrays): Lists are used to store bytes and integers. The array list is used to store bytes representing the encoded text, and the bytes_array list is used to store integers representing the binary representation of the encoded text.

File I/O: The code reads and writes data to/from files. It uses the open() function to read and write data, interacting with the underlying file system.

Binary Tree: A binary tree is constructed during the Huffman coding process. The __buildTree() method constructs the Huffman tree by repeatedly combining nodes with the lowest frequencies.
## Features

- Text compression and decompression using Huffman coding.
- Easy-to-use interface for encoding and decoding text.
- Example usage provided for quick integration.

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/RHarish1/HuffmanCode
    cd HuffmanCode
    ```

2. Compress a text file:

    ```bash
    python main.py compress input.txt
    ```

3. Decompress a binary file:

    ```bash
    python main.py decompress input.bin
    ```

## Installation

1. Make sure you have Python 3.x installed.
2. Clone the repository or download the ZIP file.
3. Navigate to the project directory.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

This implementation was inspired by the Huffman coding algorithm and its applications in data compression.

Special thanks to [Coding Ninjas](https://www.codingninjas.com/) for their insightful course, which significantly contributed to the development of this Huffman coding implementation. The knowledge gained from their course has been pivotal in creating an efficient solution.

## Contributing

Contributions are welcome! If you find any issues or have suggestions, please feel free to submit a pull request or open an issue.

## Contact

For any questions or feedback, please [contact me](mailto:harishrswamy1@gmail.com).


