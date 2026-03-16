s='I LOVE YOU'
lw=s.split()
rw=lw[ : :-1]
print(''.join(rw))

s='python love i'
s1=''.join(s.split()[::-1]).capitalize()
print(s1)
