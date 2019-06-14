
def main ():
    struct = {}
    struct['host'] = 'dir servidor'
    struct['dbname'] = 'serv_pub'
    struct['user'] =  'sop_apellido'
    struct['password'] = 'passw'

    print(', '.join([ x + '= ' + struct[x] for x in struct]))

    #print('\n'.join(["\t" * self.tab_level + self.option_list[x] for x in sorted(self.option_list)]))

                        

if __name__ == '__main__':
    main ()