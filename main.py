# source .venv/bin/activate .
from tools import parser
from tools import label 
from tools import printer
import pexpect, json, pathlib
import os


def eval_coverage_detail(target_labels: dict, tested_labels: dict):
    for kind in ["Rule", "Eq"]:
        print(f"================={kind}==================") 
        # print(tested_labels)
        for label in target_labels[kind]:
            if(label[0] in tested_labels[kind]):
                print(f"{label[0]}: TESTED")
            else:
                print(f"{label[0]}: NOT TESTED")


def eval_coverage(target_labels: dict, tested_labels: dict):
    number_of_equations = len(target_labels["Eq"])
    number_of_rewrite = len(target_labels["Rule"])
    
    number_of_passed_eq = len(tested_labels["Eq"])
    number_of_passed_rw = len(tested_labels["Rule"])
    return [number_of_equations, number_of_passed_eq, number_of_rewrite, number_of_passed_rw] 


def run_test_file(maude_path: str, file: str):
    input_path = "samples/"
    input_maude_file = file
    _ , target_labels = label.label_file(input_path + input_maude_file) 
    maude = pexpect.spawn(maude_path)
    maude.sendline('set trace on .')
    maude.sendline(f'load temp/{input_maude_file}')
    maude.sendline('quit')
    result = maude.read().decode()    
    tested_labels = parser.parse_labels(result)
    return target_labels, tested_labels
           
           
if __name__ == "__main__":
    maude_path = "Maude-3.5.1/maude -no-ansi-color"
    test_file = "test.maude"
    
    target_labels, tested_labels = run_test_file(maude_path, test_file)
    result = eval_coverage(target_labels, tested_labels)
    result.append(test_file)
    
    
    printer.print_report([result])