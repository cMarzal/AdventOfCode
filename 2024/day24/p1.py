for l in open('inp'):
    try:    a,x,b,_,c = l.split(); exec(f'{c}=lambda:{x}({a}(),{b}())')
    except: exec(l.replace(':', '=lambda:'))

print(sum(eval(f'z{i:02}()<<{i}') for i in range(46)))