import os,sys,shutil

data = {
'.component_ts' : open('samples\\patterns\\component.ts.txt', 'r').readlines(),
'.model_ts': open('samples\\patterns\\model.ts.txt', 'r').readlines(),
'public_api_ts': open('samples\\patterns\\public_api_ts.txt', 'r').readlines(),
'.module_ts': open('samples\\patterns\\module.ts.txt', 'r').readlines()
}
path = 'src\\app\\patterns'
pattern_name = input('Enter the Pattern name: ').lower()
if not os.path.exists(os.path.join(path,pattern_name)):
    os.mkdir(os.path.join(path,pattern_name))
else:
    print('pattern already exists.')
    sys.exit(0)
for file in ['.component_ts','.model_ts','public_api_ts','.module_ts']:
    new_file = open(os.path.join(path,pattern_name, (str( pattern_name if 'api' not in file else '' )+ file.replace('_','.').replace('.api','_api'))),'w')
    for line in data[file]:
        if '_ts' in file:
            lineData = line.replace('$$', pattern_name)
            lineData = lineData.replace('##', pattern_name.title())
        new_file.write(lineData)
open(os.path.join(path,pattern_name,pattern_name+'.component.html'),'w')
open(os.path.join(path,pattern_name,pattern_name+'.component.css'),'w')
shutil.copy('samples\\patterns\\index.ts', os.path.join(path,pattern_name))
