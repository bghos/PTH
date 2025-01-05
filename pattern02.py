def print_rangoli(size):
    # your code goes here
    for i in range(size-1,0,-1):

        st = ''
        # print('i:',i)
        
        for j in range(size,i,-1):
            # if i != size:
                st = st+ (chr(ord('a')+ j-1) + '-') 
        
        for j in range(i, size-1):
            st = st + (chr(ord('a')+ j+1) + '-')

        st = st.rstrip('-')
        # stright = stright.rstrip('-')
        print((st).center(size*4-3,'-'))


    
    for i in range(0,size):
        stleft:str = ''
        stright:str = ''
        stcenter = ''
        st = ''
        # print('i:',i)
        
        for j in range(size,i,-1):
            # if i != size:
                st = st+ (chr(ord('a')+ j-1) + '-') 
        
        for j in range(i, size-1):
            st = st + (chr(ord('a')+ j+1) + '-')

        st = st.rstrip('-')
        # stright = stright.rstrip('-')
        print((st).center(size*4-3,'-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)