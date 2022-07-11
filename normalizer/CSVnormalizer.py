import sys
import os
from csv import DictReader, DictWriter
from normalizer import normalizer

class CSVnormalizer(normalizer):
    def __init__(self):
        super().__init__()
        self.data = list(dict())
        self.normalized_data = self.data

    def readInputFile(self, inputFileName: str) -> None:
        '''read input csv file into data structure'''
        with open(inputFileName, 'r', encoding='utf-8', errors='replace', newline='') as f:
            self.data = list(DictReader(f))
        return

    def writeOutputFile(self, outputFileName: str) -> None:
        '''Writes normalized_data out to csv file specified by function input name'''
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
        with open(outputFileName, 'w', encoding='utf-8', newline='') as f:
            writer = DictWriter(f, fieldnames=key_order)
            writer.writeheader()
            writer.writerows(self.normalized_data)
        return

    def normalize(self, inputFileName: str, outputFileName: str):
        '''reads input csv file and writes out a normalized format csv file'''
        self.readInputFile(inputFileName)
        self.normalized_data = list()

        for i, entry in enumerate(self.data):
            skip_row = False
            for key, value in entry.items():
                try:
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
                except ValueError:
                    sys.stderr.write(f'Invalid data, skipping row {i+1}.')
                    skip_row = True
                    break
            if not skip_row:
                self.normalized_data.append(entry)

        self.writeOutputFile(outputFileName)

def main():
    if not len(sys.argv) > 1:
        sys.exit('No input file provided')

    for i, arg in enumerate(sys.argv):
        if i == 0:
            continue
        elif i == 1:
            inputName = arg
            split_inputName = os.path.splitext(inputName)
            outputName = split_inputName[0] + '_norm' + split_inputName[1]
        elif i == 2:
            outputName = arg

    norm = CSVnormalizer()
    norm.normalize(inputName, outputName)

    print(f'\nNormalized file {outputName!r} created')


if __name__ == '__main__':
    main()