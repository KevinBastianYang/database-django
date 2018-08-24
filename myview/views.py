# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render_to_response
import pymysql

# Create your views here.
back = {}
conn = pymysql.connect(host='localhost',port=3306,user="root",password="yjcGNN199726",database="PROJECT")
cur = conn.cursor()

def login(request):
    back["name"] = request.GET.get("name","null")
    return render(request, "login.html",back)

def index(request):
    return render(request,"index.html")

def team(request):
    return render(request,"team.html")

def project(request):
    return render(request,"project.html")

def search_drug(request):
    back = {}
    conn = pymysql.connect(host='localhost',port=3306,user="root",password="yjcGNN199726",database="PROJECT")
    cur = conn.cursor()
    if request.POST:
        content = str(request.POST["content"])
        if (request.POST["form"]==u'1'):
            form = "DrugBank_ID"
        elif (request.POST["form"]==u'2'):
            form = "Name"
        if (request.POST["what"]==u'1'): # drugs in drug
            sql = "SELECT DrugBank_ID,Name,CAS_Number,Drug_Type from Drug where "+form+' like "%'+content+'%"'
            cur.execute(sql)
            infors = cur.fetchall()
            results = []
            for infor in infors:
                results.append({"DrugBank_ID":infor[0],"Name":infor[1],"CAS_Number":infor[2],"Drug_Type":infor[3],"url":"drug/?id=%s"%infor[0]})
            count = len(infors)
            cur.close()
            conn.close()
            if count<>0 :
                return render(request,"search_drug.html",
                      {"type":"drug", "results":results, "count":count})
        elif (request.POST["what"]==u'2'): # combinations
            sql = "SELECT PubMed_ID, Drug_Combinations, Disease, Class, Form FROM Combination where PubMed_ID IN (SELECT PubMed_ID FROM Drug natural join Drug_Combination where "+form+' like "%'+content+'%")'
            cur.execute(sql)
            infors = cur.fetchall()
            results = []
            for infor in infors:
                results.append({"PubMed_ID":infor[0], "Drug_Combinations":infor[1], "Disease":infor[2], "Class":infor[3], "Form":infor[3], "url":"combination/?id=%s"%infor[0]})
            count = len(infors)
            cur.close()
            conn.close()
            if count <> 0:
                return render(request,"search_drug.html",
                      {"type":"combination", "results":results, "count":count})
        elif (request.POST["what"]==u'3'): # drugs in same combinations
            sql = "SELECT DrugBank_ID,Name,CAS_Number,Drug_Type from Drug where DrugBank_ID IN (SELECT DrugBank_ID FROM Drug natural join Drug_Combination where PubMed_ID in (SELECT PubMed_ID from Drug natural join Drug_Combination where "+form+' like "%'+content+'%"))'
            cur.execute(sql)
            infors = cur.fetchall()
            results = []
            for infor in infors:
                results.append({"DrugBank_ID":infor[0],"Name":infor[1],"CAS_Number":infor[2],"Drug_Type":infor[3],"url":"drug/?id=%s"%infor[0]})
            count = len(infors)
            cur.close()
            conn.close()
            if count <> 0:
                return render(request,"search_drug.html",
                          {"type":"drug", "results":results, "count":count})
        elif (request.POST["what"]==u'4'): # target
            sql = "SELECT Target_ID, Name, Gene_Name, Species from Target where Target_ID IN (SELECT Target_ID FROM Drug natural join Drug_Target where "+form+' like "%'+content+'%")'
            cur.execute(sql)
            infors = cur.fetchall()
            results = []
            for infor in infors:
                results.append({"Target_ID":infor[0], "Name":infor[1], "Gene_Name":infor[2], "Species":infor[3], "url":"target/?id=%s"%infor[0]})
            count = len(infors)
            cur.close()
            conn.close()
            if count <> 0:
                return render(request,"search_drug.html",
                          {"type":"target", "results":results, "count":count})
    #cur.close()
    #conn.close()
    return render_to_response("search_drug.html",{"type":""})

def search_com(request):
    back = {}
    conn = pymysql.connect(host='localhost',port=3306,user="root",password="yjcGNN199726",database="PROJECT")
    cur = conn.cursor()
    if request.POST:
        content = request.POST["content"]
        if (request.POST["what"] == u'1'): # combination in combination
            sql = 'select PubMed_ID,Drug_Combinations,Disease,Class,Form from Combination where PubMed_ID like "%'+content+'%"'
            cur.execute(sql)
            infors = cur.fetchall()
            results = []
            for infor in infors:
                results.append({"PubMed_ID": infor[0], "Drug_Combinations": infor[1], "Disease": infor[2], "Class": infor[3], "Form": infor[4], "url":"combination/?id=%s"%infor[0]})
            count = len(infors)
            cur.close()
            conn.close()
            if count <> 0:
                return render(request,"search_com.html",
                          {"type":"combination", "results":results, "count":count})
        elif (request.POST["what"] == u'2'): # drugs in combination
            sql = 'select DrugBank_ID,Name,CAS_Number,Drug_Type from Drug_Combination natural join Drug where PubMed_ID like"%'+content+'%"'
            cur.execute(sql)
            infors = cur.fetchall()
            results = []
            for infor in infors:
                results.append({"DrugBank_ID": infor[0], "Name": infor[1], "CAS_Number": infor[2], "Drug_Type": infor[3], "url": "drug/?id=%s"%infor[0]})
            count = len(infors)
            cur.close()
            conn.close()
            if count <> 0:
                return render(request, "search_drug.html",
                          {"type": "drug", "results": results, "count": count})
    return render(request,"search_com.html",{"type":""})

def search_target(request):
    conn = pymysql.connect(host='localhost', port=3306, user="root", password="yjcGNN199726", database="PROJECT")
    cur = conn.cursor()
    if request.POST:
        content = request.POST["content"]
        if (request.POST["form"]==u'1'):
            form = "Target_ID"
        elif (request.POST["form"]==u'2'):
            form = "Name"
        if (request.POST["what"] == u'1'): #target in target
            sql = 'select Target_ID,Name,Gene_Name,Species from target where '+form+' like"%' + content + '%"'
            cur.execute(sql)
            infors = cur.fetchall()
            results = []
            for infor in infors:
                results.append({"Target_ID": infor[0], "Name": infor[1], "Gene_Name": infor[2], "Species": infor[3], "url": "target/?id=%s"%infor[0]})
            count = len(infors)
            cur.close()
            conn.close()
            if count <> 0:
                return render(request, "search_drug.html",
                          {"type": "target", "results": results, "count": count})
        elif (request.POST['what'] == u'2'): #target -> drug
            sql = 'select DrugBank_ID,Name,CAS_Number,Drug_Type from Drug_Combination natural join Target where PubMed_ID like"%' + content + '%"'
            cur.execute(sql)
            infors = cur.fetchall()
            results = []
            for infor in infors:
                results.append({"DruBank_ID": infor[0], "Name": infor[1], "CAS_Number": infor[2], "Drug_Type": infor[3],"url": "drug/?id=%s"%infor[0]})
            count = len(infors)
            cur.close()
            conn.close()
            if count <> 0:
                return render(request, "search_drug.html",
                          {"type": "drug", "results": results, "count": count})
    return render(request,"search_target.html",{"type":""})

def drug(request):
    conn = pymysql.connect(host='localhost', port=3306, user="root", password="yjcGNN199726", database="PROJECT")
    cur = conn.cursor()
    content = str(request.GET.get("id",""))
    sql = 'select * from Drug where DrugBank_ID = "%s"'%content
    cur.execute(sql)
    infors = cur.fetchall()
    results = []
    for infor in infors:
        results.append({"DrugBank_ID": infor[0], "Name": infor[1], "CAS_Number": infor[2],
                        "Drug_Type": infor[3], "KEGG_Compound_ID": infor[4], "KEGG_Drug_ID": infor[5],
                        "PubChem_Compound_ID": infor[6], "PubChem_Substance_ID": infor[7],
                        "Smiles": infor[23], "Description": infor[24]})
    return render(request, "drug.html", results[0])

def combination(request):
    conn = pymysql.connect(host='localhost', port=3306, user="root", password="yjcGNN199726", database="PROJECT")
    cur = conn.cursor()
    content = str(request.GET.get("id",""))
    sql = 'select * from Combination where PubMed_ID = "%s"'%content
    cur.execute(sql)
    infors = cur.fetchall()
    results = []
    for infor in infors:
        results.append({"PubMed_ID": infor[0], "Drug_Combinations": infor[1], "Disease": infor[2],
                        "Class": infor[3], "Form": infor[4]})
    return render(request, "combination.html", results[0])

def target(request):
    conn = pymysql.connect(host='localhost', port=3306, user="root", password="yjcGNN199726", database="PROJECT")
    cur = conn.cursor()
    content = str(request.GET.get("id",""))
    sql = 'select * from Target where Target_ID = "%s"'%content
    cur.execute(sql)
    infors = cur.fetchall()
    results = []
    for infor in infors:
        results.append({"Target_ID": infor[0], "Name": infor[1], "Gene_Name": infor[2],
                        "GeneBank_Protain_ID": infor[3], "GeneBank_Gene_ID": infor[4],
                        "Uniprot_Title": infor[6], "GeneCard_ID": infor[8],
                        "GenAtlas_ID": infor[9], "HGNC_ID": infor[10],
                        "Species": infor[11], "Target_Description": infor[12],
                        "Target_Sequence": infor[13]})
    return render(request, "target.html", results[0])

cur.close()
conn.close()