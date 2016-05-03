from ROOT import *
import sys,os
gROOT.SetBatch(True)
hists = ['ttbar_2lCR_mbb_met100_hists.root:h_lep_dilep_event_MCT_2lCR_mbb_met100',
         'ttbar_2lCR_mbb_met200_hists.root:h_lep_dilep_event_MCT_2lCR_mbb_met200']
title = 'test'
legends = ['hist1','hist2']
logscale = False
rebin = 25
print "Overlaying these hists: ",hists
print "Title for the plot is: ",title
print "Using legends : ",legends

files=[]
keys = []
for item in hists:
    filename = item.split(":")[0]
    keys.append(item.split(":")[1])
    fhist = TFile(filename)
    files.append(fhist)

c = TCanvas("c", "c")
c.SetWindowSize(600, 600)
if logscale:c.SetLogy()
l = TLegend(.3, .7, .9, .9)
s = THStack(title, title)
colors = [kBlue,kRed,kCyan-3,kOrange-2,kMagenta-5]

hists = []
for i,k in enumerate(keys):
    hist = files[i].Get(k) 
    print k
    if not hist.InheritsFrom("TH1"):
        continue

    if hist.Integral(): hist.Scale(1/hist.Integral())

    hist.SetLineColor(colors[i])
    hist.SetMarkerColor(colors[i])
    hist.SetLineWidth(2)
    hist.Rebin(rebin)
    hist.SetTitle(legends[i])

    s.Add(hist)
    
#    l.Clear()
    l.AddEntry(hist)

s.Draw("nostack")
s.GetXaxis().SetTitle(title+' [GeV]')
l.SetTextSize(0.03)
l.Draw()

c.Update()
c.SaveAs("./"+title+".pdf")
