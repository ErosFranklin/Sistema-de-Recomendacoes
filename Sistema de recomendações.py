def operador(tf, quant):
    for n in range(1, quant + 1):
        print('Qual o nome do ', n, 'º filme? ', sep='', end='')
        tf.append(input())
    return tf


def filmes_usuario1(fu1, tf):
    for i in tf:
        print('Você já assistiu o filme \033[1;4m{}\033[m?[S/N] '.format(i), sep='', end='')
        fu1.append(str(input()))
    return fu1


def filmes_usuario2(fu2, tf):
    for i in tf:
        print('Você já assistiu o filme \033[1;4m{}\033[m?[S/N] '.format(i), sep='', end='')
        fu2.append(str(input()))
    return fu2


print('=-' * 30)
print('                     Área do Operador        ')
print('=-' * 30)

filmes = []
quant_film = 10
total_filmes = operador(filmes, quant_film)

print('=-' * 30)
print('                     Área Usuário 1        ')
print('=-' * 30)

filmes_user1, assistidos_user1 = [], []
total_filmes_user1 = filmes_usuario1(filmes_user1, total_filmes)

for f1 in total_filmes_user1:
    if f1 in 'Ss':
        assistidos_user1.append(True)
    elif f1 in 'Nn':
        assistidos_user1.append(False)

print('=-' * 30)
print('                     Área Usuário 2        ')
print('=-' * 30)

filmes_user2, assistidos_user2 = [], []
total_filmes_user2 = filmes_usuario2(filmes_user2, total_filmes)

for f2 in total_filmes_user2:
    if f2 in 'Ss':
        assistidos_user2.append(True)
    elif f2 in 'Nn':
        assistidos_user2.append(False)

print('=-' * 30)
print('                     Recomendação       ')
print('=-' * 30)

recomendacao_user1, recomendacao_user2 = [], []

for r in range(quant_film):
    if assistidos_user1[r] is False and assistidos_user2[r] is True:
        recomendacao_user1.append(total_filmes[r])
    if assistidos_user1[r] is True and assistidos_user2[r] is False:
        recomendacao_user2.append(total_filmes[r])
    elif assistidos_user1[r] is False and assistidos_user2[r] is False:
        print('Não temos nenhuma recomendação até o momento...')
        break

print('Recomendações para o Usuário 1: ', end='')
for r1 in recomendacao_user1:
    print('\033[1;4m{}\033[m'.format(r1), end=' | ')
print()
print('Recomendações para o Usuário 2: ', end='')
for r2 in recomendacao_user2:
    print('\033[1;4m{}\033[m'.format(r2), end=' | ')
