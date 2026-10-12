from fastapi_offline import FastAPIOffline

app = FastAPIOffline()

mylist = [100, 200, 300, 200]

@app.get('/home/')
def say_hello():
    return {'HELLO': 'WORLD'}


@app.get('/getItems/')
def get_items():
    return {'output': mylist}

@app.get('/getLastItems')
def get_last_item():
    if len(mylist) > 0:
        return {'output': mylist[-1]}
    else:
        return {'List Is Empty'}

@app.post('/addItem/{new_item}')
def insert_item(new_item:int):
    mylist.append(new_item)
    return {'new output': mylist}


@app.delete('/removeItem/')
def remove_item(item:int):
    if item in mylist:
        mylist.remove(item)
        return {'list after remove': mylist}
    else:
        return {f'{item} not found in list'}

@app.delete('/removeIndexItem/')
def index_item(index: int):
    if index >= 0 and index < len(mylist):
        print(mylist)
        r = mylist.pop(index)
        return {f'{r} deleted from list'}
    else:
        return {f'{r} not found in list'}

@app.put('/updateItem/')
def update_item(index: int, new_item: int):
    if index >=0 and index < len(mylist):
        mylist[index] = new_item
        return {'updated list': mylist}
    else:
        return {f'index of {index}, not exist in my list'}


@app.put('/updateWithItem')
def update_in_item(item: int , new_item: int):
    if item in mylist:
        i = mylist.index(item) 
        mylist[i] = new_item
        return {'updated list': mylist}
    else:
        return {f'index of {item}, not exist in my list'}
        