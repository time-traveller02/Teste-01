h = float(input('Digite a altura da parede em metros:'))
l = float(input('Digite a largura da parede em metros:'))
a = h * l 
t = a / 2
print('Sua parede é de dimensões {}x{} e sua área é {}m².'.format(h, l, a))
print('Para pintar essa parede voçe precisará de {}L de tinta.'.format(t))
