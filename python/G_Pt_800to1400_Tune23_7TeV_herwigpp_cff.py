import FWCore.ParameterSet.Config as cms

from Configuration.Generator.HerwigppDefaults_cfi import *

generator = cms.EDFilter("ThePEGGeneratorFilter",
	herwigDefaultsBlock,
	crossSection = cms.untracked.double(3.982027e-03),
	filterEfficiency = cms.untracked.double(1),

	configFiles = cms.vstring(),
	parameterSets = cms.vstring(
		'cm7TeV',
		'pdfMRST2001',
		'productionParameters',
		'basicSetup',
		'setParticlesStableForDetector',
	),
	productionParameters = cms.vstring(
		'cd /Herwig/MatrixElements/',
		'insert SimpleQCD:MatrixElements[0] MEGammaJet',

		'cd /',
		'set /Herwig/Cuts/JetKtCut:MinKT 800 *GeV',
		'set /Herwig/Cuts/JetKtCut:MaxKT 1400*GeV',
		'set /Herwig/Cuts/QCDCuts:MHatMin 0.0*GeV',
		'set /Herwig/Cuts/PhotonKtCut:MinKT 0.0*GeV',
		'set /Herwig/Cuts/PhotonKtCut:MinEta -5',
		'set /Herwig/Cuts/PhotonKtCut:MaxEta 5',
	),
)

configurationMetadata = cms.untracked.PSet(
	version = cms.untracked.string('\$Revision$'),
	name = cms.untracked.string('\$Source$'),
	annotation = cms.untracked.string('Summer2011 sample with HERWIGPP: Prompt photon production, pThat = 800 .. 1400 GeV, Tune23')
)