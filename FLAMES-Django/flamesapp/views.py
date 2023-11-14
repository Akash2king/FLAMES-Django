from django.shortcuts import render, HttpResponse

def FLAMES(request):
    if request.method == 'POST':
        boy_name = request.POST['boyname'].lower()
        girl_name = request.POST['girlname'].lower()

        if boy_name and girl_name:
            n = len(set(boy_name).intersection(girl_name))

            flames = ["Friends", "Lovers", "Affection", "Marriage", "Enemies", "Siblings"]
            temp = n
            c = 1

            while len(flames) != 1:
                for i in range(len(flames)):
                    if (n > len(flames)) and (c == 1):
                        temp = n - len(flames)
                        if i == (temp - 1):
                            try:
                                del flames[i]
                                flames = flames[i:] + flames[:i]
                            except:
                                if temp > len(flames):
                                    temp = temp - len(flames)
                                    c += 1
                    else:
                        if i == temp - 1:
                            del flames[i]
                            flames = flames[i:] + flames[:i]

            relation = flames[0]
            return render(request, 'flames.html', {'relation': relation, 'i': True, 'boy': boy_name, 'girl': girl_name})

    return render(request, 'flames.html')
