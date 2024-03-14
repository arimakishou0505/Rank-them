from django.shortcuts import render, redirect
from .models import Target, Group
from .forms import TargetForm
from .forms import GroupForm


def index(request):
    targets = Target.objects.all()
    for target in targets:
        target.total_votes = target.up_votes - target.down_votes  # 仮想的な 'total_votes' フィールドを計算
    sorted_targets = sorted(targets, key=lambda x: x.total_votes, reverse=True)  # 投票数の降順でソート
    groups = Group.objects.all() 
    return render(request, 'voting/index.html', {'groups': groups, 'targets': sorted_targets})

def upvote(request, target_id):
    target = Target.objects.get(pk=target_id)
    target.up_votes += 1
    target.save()
    return redirect('voting:index')

def downvote(request, target_id):
    target = Target.objects.get(pk=target_id)
    target.down_votes += 1
    target.save()
    return redirect('voting:index')

def add_target(request):
    if request.method == 'POST':
        form = TargetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('voting:index')  # リダイレクト先を適切なURLに変更する
    else:
        form = TargetForm()
    return render(request, 'voting/add_target.html', {'form': form})

def add_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin:index')  # 適切な管理者ページへのリダイレクト先を指定します
    else:
        form = GroupForm()
    return render(request, 'voting/add_group.html', {'form': form})

def group_targets(request, group_name):
    group = Group.objects.get(name=group_name)
    targets = Target.objects.filter(group=group)
    return render(request, 'voting/group_targets.html', {'group': group, 'targets': targets})

def soccer_player_targets(request):
    group = Group.objects.get(name='soccer player')
    targets = Target.objects.filter(group=group)
    return render(request, 'voting/soccer_player_targets.html', {'targets': targets})