
LETTER_GRADES = 'ABCDF'


def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as text_file:  # can throw FileNotFoundError
        result = tuple(l.rstrip() for l in text_file.readlines())
        return result
    
    
#just for testing
def write_text_file(file_path, line_list):
    f = open(file_path, 'w', encoding='utf-8')
    # write to file
    for line in line_list:
        f.write(line + '\n')
    # cleanup
    f.close()
    
# SPNG 2016 UGRD FR-EL ENG
def line_is_semester_header(input_line):
    split_line = input_line.split(" ")
    
    if len(split_line) >= 3 and split_line[2] == 'UGRD':
        return True
    return False


def line_is_semester_footer(input_line):
    if input_line == ' Hrs Att Hrs Ern Qual Pts GPA':
        return True
    return False
    
    
    
    
def trim_non_umr_lines(input_lines):
    umr_lines = []
    
    for line_num in range( len( input_lines ) ):
        
        if line_is_semester_header(input_lines[line_num]):
            line_num += 1
            
            #append lines until you hit semester footer
            while(line_is_semester_footer(input_lines[line_num]) == False and line_num < len(input_lines)):
                umr_lines.append(input_lines[line_num])
                line_num += 1
                
    return umr_lines
            
            
    
    
def trim_non_gpa_lines(umr_lines):
    gpa_lines = []
    
    for umr_line in umr_lines:
        split_umr_line = umr_line.split(" ")
        
        if split_umr_line[-2] in LETTER_GRADES:
            gpa_lines.append(umr_line)
    
    return gpa_lines
        
        
LETTER_TO_POINTS_D = {'A': 4,
                      'B': 3,
                      'C': 2,
                      'D': 1,
                      'F': 0,}
    
def letter_grade_to_points(letter_grade):
    return LETTER_TO_POINTS_D[letter_grade]
    
    
    

def build_gpa_info_dl(gpa_lines):
    gpa_info_dl = []
    
    for gpa_line in gpa_lines:
        split_gpa_line = gpa_line.split(" ")
        
        letter_grade = split_gpa_line[-2]
        
        gpa_info_dl.append({'hours'              : float(split_gpa_line[-1]),
                            'letter_grade_points': letter_grade_to_points(letter_grade)})
    
    return gpa_info_dl
    
    
    
def get_set_in_stone_umr_hours_taken(gpa_info_dl):
    hours = 0
    for gpa_info_d in gpa_info_dl:
        hours += gpa_info_d['hours']
    return hours
    
    
def get_total_points(gpa_info_dl):
    points = 0
    for gpa_info_d in gpa_info_dl:
        points += gpa_info_d['letter_grade_points'] * gpa_info_d['hours']
    return points
    
    
    
    

input_filename = 'input.txt'
output_test_path = 'output_test.txt'

input_lines = read_text_file(input_filename);
# print(input_lines)
umr_lines = trim_non_umr_lines(input_lines)
# print (umr_lines) 
# write_text_file(output_test_path, umr_lines)

gpa_lines = trim_non_gpa_lines(umr_lines)
# print (gpa_lines) 
# write_text_file(output_test_path, gpa_lines)

gpa_info_dl = build_gpa_info_dl(gpa_lines)
# print (gpa_info_dl) 
# write_text_file(output_test_path, gpa_lines)

set_in_stone_umr_hours_taken = get_set_in_stone_umr_hours_taken(gpa_info_dl)

total_points = get_total_points(gpa_info_dl)

set_in_stone_umr_gpa = total_points / set_in_stone_umr_hours_taken


print('set_in_stone_umr_hours_taken: ', set_in_stone_umr_hours_taken) 
print('set_in_stone_umr_gpa: ', set_in_stone_umr_gpa)













