# Generate bed files, for Awk exercise

library(Homo.sapiens)
library(dplyr)

chr8 = genes(TxDb.Hsapiens.UCSC.hg19.knownGene) %>% subset(seqnames=='chr8')
chr8$symbol = AnnotationDbi::select(org.Hs.eg.db, key=chr8$gene_id, keytype='ENTREZID', columns='SYMBOL')$SYMBOL<Paste>
chr8$exerc1 = ifelse(start(chr8)>5000000 & end(chr8) < 10000000, T, F)

