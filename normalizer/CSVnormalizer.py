import sys
import os
from codecs import open as codecs_open
from csv import DictReader, DictWriter
from normalizer import normalizer

class CSVnormalizer(normalizer):
    def __init__(self):
        super().__init__()
        self.data = list(dict())
        self.normalized_data = self.data

    def readInputFile(self, inputFileName: str) -> None:
        with codecs_open(inputFileName, 'r', encoding='utf-8', errors='replace') as f:
            self.data = list(DictReader(f))
        return

    def writeOutputFile(self, outputFileName: str) -> None:
        key_order = (
            'Timestamp',
            'Address',
            'ZIP',
            'FullName',
            'FooDuration',
            'BarDuration',
            'TotalDuration',
            'Notes',
        )
        with codecs_open(outputFileName, 'w', encoding='utf-8') as f:
            writer = DictWriter(f, fieldnames=key_order)
            writer.writeheader()
            writer.writerows(self.normalized_data)
        return

    def normalize(self, inputFileName: str, outputFileName: str):
        '''reads input csv file and writes out a normalized format csv file'''
        
        self.readInputFile(inputFileName)
        self.normalized_data = self.data

        for i, entry in enumerate(self.normalized_data):
            for key, value in entry.items():
                match key:
                    case 'Timestamp':
                        entry[key] = self.normalize_timestamp(value)
                    case 'ZIP':
                        entry[key] = self.normalize_zipcode(value)
                    case 'FullName':
                        entry[key] = self.normalize_fullname(value)
                    case 'FooDuration' | 'BarDuration':
                        entry[key] = self.normalize_duration(value)
                    case 'TotalDuration':
                        entry[key] = self.normalize_totalDuration(entry['FooDuration'], entry['BarDuration'])
            self.normalized_data[i] = entry

        self.writeOutputFile(outputFileName)

def main():
    print()
    inputName = os.path.join('test','sample.csv')
    outputName = os.path.join('test','sample_out.csv')
    
    for i, arg in enumerate(sys.argv):
        if i == 0:
            continue
        elif i == 1:
            inputName = sys.argv[i]
            split_inputName = os.path.splitext(inputName)
            outputName = split_inputName[0] + '_out' + split_inputName[1]
        elif i == 2:
            outputName = sys.argv[i]

    norm = CSVnormalizer()
    norm.normalize(inputName, outputName)

    print('end...')


if __name__ == '__main__':
    main()