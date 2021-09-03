# this is created by programer 


from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'indexBootstrap.html')
    # return render(request, 'index.html')
    # return HttpResponse('<h1> welcome to Text Utils !!</h1>')

def analyzed_page(request):

    # get the text  from text area 
    input_text = request.GET.get('inputText', 'NO DATA To Analyze')

    # get switches values 
    remove_punc = request.GET.get('remove_punctuation', 'off')
    all_capital = request.GET.get('all_capital', 'off')
    new_line_remove = request.GET.get('new_line_remove', 'off')
    extra_space_remove = request.GET.get('extra_space_remove', 'off')

    print(input_text)
    print(remove_punc)
    if remove_punc == 'on':
        Analyzed = ""
        punctuations = '''!()-[];:'",<>./?@#$%^&*_~'''
        for char in input_text:
            if char not in punctuations:
                Analyzed += char
        input_text = Analyzed

        # varaibles declaration 
        parameters = {
            'purpose' : 'Remove Punctuations',
            'analyzed_text' : Analyzed,  
        }

    if all_capital == 'on':
        Analyzed = ""
        for char in input_text:
            Analyzed += char.upper()
        input_text = Analyzed
        # varaibles declaration 
        parameters = {
            'purpose' : 'Upper case convertion',
            'analyzed_text' : Analyzed,  
        }
    if new_line_remove == 'on':
        Analyzed = ""
        for char in input_text:
            if char != '\n' and char != '\r':
                Analyzed += char
        input_text = Analyzed
        # varaibles declaration 
        parameters = {
            'purpose' : 'Remove removed newlines',
            'analyzed_text' : Analyzed,  
        }
    if extra_space_remove == 'on':
        Analyzed = ""
        for index,char in enumerate(input_text):
            if input_text[index] == " " and input_text[index+1] == ' ':
                pass
            else:
                Analyzed += char
        input_text = Analyzed
        # varaibles declaration 
        parameters = {
            'purpose' : 'Rmove Extra Spaces',
            'analyzed_text' : Analyzed,  
        }

    return render(request, 'remove_punctuation.html', parameters)
    
        
    # return HttpResponse('this is all remove punctuations Text Utils')


