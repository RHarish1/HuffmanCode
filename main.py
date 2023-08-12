import heapq,os

class BinaryTreeNode:
    def __init__(self,value,frequency):
        self.value=value
        self.frequency=frequency
        self.right=None
        self.left=None
    def __lt__(self,other):
        return self.frequency<other.frequency
    def __eq__(self,other):
        return self.frequency<other.frequency

class HuffmannCoding:
    
    def __init__(self,path):
        self.path=path
        self.__heap=[]
        self.__codes={}
        self.__reversecodes={}
    
    def __make_frequency_dict(self,text):
        #Storing characters along with their frequencies 
        frequency_dict={}
        for char in text:
            if char not in frequency_dict:
                frequency_dict[char]=0
            frequency_dict[char]+=1
        return frequency_dict
    
    def __buildHeap(self,freq_dict):
        #Making a minimum heap to get the minimum frequencies as and when required
        for key in freq_dict:
            frequency=freq_dict[key]
            binary_tree_node=BinaryTreeNode(key,frequency)
            heapq.heappush(self.__heap,binary_tree_node)
    
    def __buildTree(self):
        #Get minimum Two Values and push it in with " " and Sum of both until only one is left with us
        while len((self.__heap)>1):
            binary_tree_node1=BinaryTreeNode(heapq.heappop(self.__heap))
            binary_tree_node2=BinaryTreeNode(heapq.heappop(self.__heap))
            freq_sum=binary_tree_node1.freq+binary_tree_node2.frequency
            newNode=BinaryTreeNode(None,freq_sum)
            newNode.left=binary_tree_node1
            newNode.right=binary_tree_node2
            heapq.heappush(self.__heap,newNode)
        return
    
    def __buildCodesHelper(self,root,curr_bits):
        if root is None:
            return
        if root.value is not None:
            self.__codes[root.value]=curr_bits
            self.__reversecodes[curr_bits]=root.value
            return 
        self.__buildCodesHelper(root.left,curr_bits+"0")
        self.__buildCodesHelper(root.right,curr_bits+"1")
       
    def __buildCodes(self):
        #Make the left move 0 and the right move 1 and store the code
        root=heapq.heappop(self.__heap)
        self.__buildCodesHelper(root,"")
    
    def __getEncodedText(self,text):
        EncodedText=""
        for char in text:
            EncodedText+=self.__codes[char]
        return EncodedText
    def __getPaddedEncodedText(self,EncodedText):
        padded_amount=8-(len(encoded_text))
        for i in range(padded_amount):
            encoded_text+="0"
        padded_info=("{0:08b}").format(padded_amount)
        padded_encoded_text=padded_info+encoded_text
        return padded_encoded_text
    
    def __getBytesArray(self,padded_encoded_text):
        array=[]
        for i in range(0,len(padded_encoded_text),8):
            bytes=padded_encoded_text[i:i+8]
            array.append(int(bytes,2))
        return array
    
    def compress(self):
        #get file and read from file
        filename,file_extension=os.path.splitext(self.path)
        output_path=filename+".bin"
        with open(self.path,"r+") as file,open(output_path,"wb") as output:
            text=file.read()
            text=text.rstrip()
            #make frequency dictionary
            freq_dict=self.__make_frequency_dict
            #constructing the heap
            self.__buildHeap[freq_dict]
            #Constructing binary tree from heap 
            self.__buildTree()
            #Construct Codes from binary tree
            self.__buildCodes()
            #Create the encoded text using codes
            encoded_text=self.__getEncodedText(text)
            #Put this encoded text into binary file, file adds extra 0s to make it 8 bit multiple long fix it, store number of added 0s
            #later we remove these 0s
            #Pad this encoded text
            padded_encoded_text=self.__getPaddedEncodedText(encoded_text)
            #convert into byters
            bytes_array=self.__getBytesArray(padded_encoded_text)
            #return this binary file as output
            final_bytes=bytes(bytes_array)
            output.write(final_bytes)
        print("Compressed")
        return output_path
    
    def __removePadding(self,text):
        padded_info=text[:8]
        extra_padding=int(padded_info,2)
        text=text[8:]
        text_after_padding_removed=text[:-1*extra_padding]
        return text_after_padding_removed

    def __decodeText(self,text):
        decoded_text=""
        current_bit=""
        for bit in text:
            current_bit+=bit
            if current_bit in self.__reversecodes:
                decoded_text+=self.__reversecodes[current_bit]
                current_bit=""
        return decoded_text

    def decompress(self,input_path):
        filename,file_extension=os.path.splitext(self.path)
        output_path=filename+"_decompressed"+".txt"
        with open(self.path,"rb") as file,open(output_path,"w") as output:
            bit_string=""
            byte=file.read(1)
            while byte:
                byte=ord(byte)
                bits=bin(byte)[2:].rjust(8,'0')
                bit_string+=bits
                byte=file.read(1)
            #removing the last extra 0s from the amount of 0s we got from first 8 bits
            actual_text=self.__removePadding(bit_string)
            decompressed_text=self.__decodeText(actual_text)
            output.write(decompressed_text)
        return
