from ROOT import *
gROOT.SetBatch(True)


fZee = TFile("/Users/mliu/Downloads/ttbar_2lCR_mbb_hists.root")

c = TCanvas("c", "c")
c.SetWindowSize(800, 600)

for k in fZee.GetListOfKeys():
    hZee = fZee.Get(k.GetName())
    
    if not hZee.InheritsFrom("TH2"):
        continue

    hZee.SetTitle("ttz")

    hZee.GetXaxis().SetTitle(k.GetName())
    hZee.Draw("colz")

    c.Update()
    c.SaveAs(histname+".pdf")
