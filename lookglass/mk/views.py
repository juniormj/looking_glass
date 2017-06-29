from django.shortcuts import render, render_to_response
from .forms import FormMK
from paramiko import SSHClient, AutoAddPolicy
import time
from django.core.context_processors import csrf
from django.template import RequestContext


cidr = ""
def index(request):
    form = FormMK()
    return render_to_response('index.html', {'form': form}, context_instance=RequestContext(request))
#    return render(request, "index.html")


def resultado(request):


    #Conexao com o Mikrotik
#    host = ("192.168.155.13")
    host = ("192.168.10.2")
    user = ("admin")
    password = (" ")
    sshCli = SSHClient()
    sshCli.set_missing_host_key_policy(AutoAddPolicy())
    sshCli.connect(str(host), port=22, username=str(user), password=str(password))
    
    #Pega os dados do Formulario  
    if request.method=='POST':
        form = FormMK(request.POST)
        if form.is_valid():
	  
            cidr=form.cleaned_data.get('cidr')
            
            if form.cleaned_data.get('opcao') == '1':
                stdin, stdout, stderr = sshCli.exec_command('ip route print detail where dst-address in '+cidr) 
                line = stdout.readlines()
                return render_to_response('saida.html', {'line': line})
            elif form.cleaned_data.get('opcao') == '2':
                stdin, stdout, stderr = sshCli.exec_command('ping count=5 '+cidr) 
                line = stdout.readlines()
                return render_to_response('saida.html', {'line': line})
            elif form.cleaned_data.get('opcao') == '3':
                stdin, stdout, stderr = sshCli.exec_command('tool traceroute '+cidr) 
                line = stdout.readlines()
                return render_to_response('saida.html', {'line': line})
            elif form.cleaned_data.get('opcao') == '4':
                stdin, stdout, stderr = sshCli.exec_command('ipv6 route print detail where dst-address in '+cidr) 
                line = stdout.readlines()
                return render_to_response('saida.html', {'line': line})
            elif form.cleaned_data.get('opcao') == '5':
                stdin, stdout, stderr = sshCli.exec_command('ping count=5 '+cidr) 
                line = stdout.readlines()
                return render_to_response('saida.html', {'line': line})
            elif form.cleaned_data.get('opcao') == '6':
                stdin, stdout, stderr = sshCli.exec_command('tool traceroute '+cidr) 
                line = stdout.readlines()
                return render_to_response('saida.html', {'line': line})

    else:
        form = FormMK()
    return render_to_response('index.html', {'form': form}, context_instance=RequestContext(request))

 
    time.sleep(1)
    sshCli.close()
    
    
