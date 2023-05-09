from ast import Return
import pandas as pd
from flask import Flask,request,render_template
import warnings
warnings.filterwarnings("ignore")
d=r'Results1.xlsx'
r=pd.read_excel(d)
df=pd.DataFrame(r)

app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def test():
    if request.method=='POST':
        form=request.form
        htno=(str(form['htno'])).upper()
        a=r['HTNO'].values==htno
        b=df[a]
        c=df[a]
        c.reset_index(drop=True, inplace=True)
        c.index.name='Sl_NO.'
        c.index=c.index+1
        grade={'ABSENT':0,'COMPLE':10,'MP':0,'A+':10,'A':9,'B':8,'C':7,'D':6,'E':5,'F':0}
        b.GRADE=[grade[item] for item in b.GRADE]
        b=b.assign(GC=b.GRADE*b.CREDITS)
        sgpa=b['GC'].sum()/b['CREDITS'].sum()
        if 'F'in c.GRADE.values.tolist():
            hey='FAIL'
            per=''
            gpa=''
        else:
            hey='PASS'
            per=(sgpa*10-7.5).round(2)
            gpa=sgpa.round(2)
        disp=c[['SUBNAME','GRADE','CREDITS','INTERNALS']].to_html()  
        return render_template('page.html',res=disp,status=hey,perc=per,SGPA=gpa,htno=htno)
    return render_template('page.html',res='enter hall ticket number' , status='')
if __name__=='__main__':
    app.run(debug=True)
