definition = {
'STOCK_MRKT_CD' : 6,
'ACPLC_LNGG_STOCK_MRKT_NM' : 60,
'ENGLS_STOCK_MRKT_NM' : 60,
'HB_NTN_CD' : 3,
'LSTNG_CD' : 12,
'ACPLC_LNGG_ENTRP_NM' : 100,
'ENGLS_ENTRP_NM' : 100,
'OVRSS_ENTRP_CRPRT_RGNO' : 50,
'OVRSS_ENTRP_BSNSM_RGNO' : 50,
'FNDTN_DT' : 8,
'LSTNG_DT' : 8,
'ACPLC_LNGG_INDST_GNNM' : 100,
'ENGLS_INDSTRSCTRS_NM' : 100,
'CRRNC_SCTIN_CD' : 3,
'ACCNN_YR' : 4,
'REPRT_KIND_CD' : 1,
'STACNT_DT' : 8,
'BSN_PRFT_RT_VAL' : 4,
'BSN_PRFT_INCRE_RT_VAL' : 4,
'THTRM_NTPF_INCRE_RT_VAL' : 4,
'ENTRP_YRMN_GRRT_VAL' : 4,
'ENTRP_RELTN_TDNGS_DT' : 8,
'ENTRP_RELTN_TDNGS_KIND_CONT' : 10,
'ENTRP_RELTN_TDNGS_SUBJC' : 100,
'ENTRP_RELTN_TDNGS_CONT_SMMR' : 1000,
'ENTRP_RELTN_TDNGS_DTL_CONT' : 4000,
'INFO_ORGIN_CONT' : 4000,
'ENTRP_RELTN_TDNGS_URL' : 1000,
'CMP_INSD_RELTN_INFO' : 4000,
'CSTMR_RELTN_INFO' : 4000,
'SPPL_RELTN_INFO' : 4000,
'CMPTT_RELTN_INFO' : 4000,
'SBST_GOODS_RELTN_INFO' : 4000,
'OPERT_SCTIN_CD' : 1,
'DATA_CRTIN_DT' : 8,
'CNTCT_PRCES_STTS_CD' : 1,
'CNTCT_PRCES_DT': 8}

ColumnsDict = {
"날짜" : "ENTRP_RELTN_TDNGS_DT",
"종류" : "ENTRP_RELTN_TDNGS_KIND_CONT",
"제목" : "ENTRP_RELTN_TDNGS_SUBJC",
"요약" : "ENTRP_RELTN_TDNGS_CONT_SMMR",
"상세" : "ENTRP_RELTN_TDNGS_DTL_CONT",
"출처" : "INFO_ORGIN_CONT",
"URL" : "ENTRP_RELTN_TDNGS_URL",
"사내" : "CMP_INSD_RELTN_INFO",
"고객" : "CSTMR_RELTN_INFO",
"공급" : "SPPL_RELTN_INFO",
"경쟁" : "CMPTT_RELTN_INFO",
"대체" : "SBST_GOODS_RELTN_INFO"}

Financial = ["CUASS_AMT", "NNCRRNT_ASSTS_AMT", "CASH_AND_DPST_AMT", "SCRTS_AMT",
    "LON_BOND_AMT", "INSTM_FNC_ASSTS_AMT", "LEASE_ASSTS_AMT", "TPE_ASSTS_AMT",
    "ETC_ASSTS_AMT", "ASSTS_SUMM", "FLTNG_DEBT_AMT", "NNCRRNT_DEBT_AMT",
    "CSTDPSLBLITS_AMT", "CSTDBT_AMT", "ETC_DEBT_AMT", "DEBT_SUMM", "CAPTL",
    "CAPTL_SRPL","CAPTL_MDTN_AMT", "ETC_INCLSN_PRLSS_ACTTL_AMT", "PRFT_SRPL", "CAPTL_SUMM",
    "DEBT_CAPTL_SUMM_AMT", "PRSLS", "SLLNG_PRMPC_AMT", "BSN_COST_AMT", "BSN_PRFT_AMT",
    "BSN_ELSE_COST_AMT", "CTAX_COST_STRBF_NTINCMLS_AMT", "CTAX_COST_STRBF_CNTNTBS_PLAMT",
    "CTAX_COST_AMT", "CNTNTBS_PRLSS_CTAX_COST_AMT", "CNTNTBS_PRFT_AMT",
    "DSCNT_BSNSS_PRLSS_AMT", "THTRM_NTPF_AMT", "BSN_ACTI_CSFLW_AMT",
    "INVSM_ACTI_CASH_INFL_AMT", "FNNR_ACTI_CASH_INFL_AMT", "CASH_INCRE_AMT",
    "BSIS_CASH_AMT","ENTRM_CASH_AMT", "DEBT_RATE", "PRSLS_INCRE_RT"]

Month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

NumericList = ["STACNT_DT","CUASS_AMT", "NNCRRNT_ASSTS_AMT", "CASH_AND_DPST_AMT", "SCRTS_AMT", "LON_BOND_AMT", "INSTM_FNC_ASSTS_AMT", "LEASE_ASSTS_AMT", "TPE_ASSTS_AMT", "ETC_ASSTS_AMT", "ASSTS_SUMM", "FLTNG_DEBT_AMT", "NNCRRNT_DEBT_AMT", "CSTDPSLBLITS_AMT", "CSTDBT_AMT", "ETC_DEBT_AMT", "DEBT_SUMM", "CAPTL",
"CAPTL_SRPL", "CAPTL_MDTN_AMT", "ETC_INCLSN_PRLSS_ACTTL_AMT", "PRFT_SRPL", "CAPTL_SUMM", "DEBT_CAPTL_SUMM_AMT", "PRSLS", "SLLNG_PRMPC_AMT", "BSN_COST_AMT", "BSN_PRFT_AMT", "BSN_ELSE_COST_AMT", "CTAX_COST_STRBF_NTINCMLS_AMT", "CTAX_COST_STRBF_CNTNTBS_PLAMT", "CTAX_COST_AMT", "CNTNTBS_PRLSS_CTAX_COST_AMT",
"CNTNTBS_PRFT_AMT", "DSCNT_BSNSS_PRLSS_AMT", "THTRM_NTPF_AMT", "BSN_ACTI_CSFLW_AMT", "INVSM_ACTI_CASH_INFL_AMT", "FNNR_ACTI_CASH_INFL_AMT", "CASH_INCRE_AMT", "BSIS_CASH_AMT", "ENTRM_CASH_AMT", "DEBT_RATE", "PRSLS_INCRE_RT"]

MonthDict = {
"Jan" : "01",
"Feb" : "02",
"Mar" : "03",
"Apr" : "04",
"May" : "05",
"Jun" : "06",
"Jul" : "07",
"Aug" : "08",
"Sep" : "09",
"Oct" : "10",
"Dec" : "11",
"Nov" : "12"
}

TableDefaultColumns ={
"표준_영문컬럼명":[
'keyval',
'stock_mrkt_cd',
'acplc_lngg_stock_mrkt_nm',
'engls_stock_mrkt_nm',
'hb_ntn_cd',
'lstng_cd',
'acplc_lngg_entrp_nm',
'engls_entrp_nm',
'ovrss_entrp_crprt_rgno',
'ovrss_entrp_bsnsm_rgno',
'fndtn_dt',
'lstng_dt',
'acplc_lngg_indst_gnnm',
'engls_indstrsctrs_nm',
'crrnc_sctin_cd',
'accnn_yr',
'reprt_kind_cd',
'stacnt_dt',
'cuass_amt',
'nncrrnt_assts_amt',
'cash_and_dpst_amt',
'scrts_amt',
'lon_bond_amt',
'instm_fnc_assts_amt',
'lease_assts_amt',
'tpe_assts_amt',
'etc_assts_amt',
'assts_summ',
'fltng_debt_amt',
'nncrrnt_debt_amt',
'cstdpslblits_amt',
'cstdbt_amt',
'etc_debt_amt',
'debt_summ',
'captl',
'captl_srpl',
'captl_mdtn_amt',
'etc_inclsn_prlss_acttl_amt',
'prft_srpl',
'captl_summ',
'debt_captl_summ_amt',
'prsls',
'sllng_prmpc_amt',
'bsn_cost_amt',
'bsn_prft_amt',
'bsn_else_cost_amt',
'ctax_cost_strbf_ntincmls_amt',
'ctax_cost_strbf_cntntbs_plamt',
'ctax_cost_amt',
'cntntbs_prlss_ctax_cost_amt',
'cntntbs_prft_amt',
'dscnt_bsnss_prlss_amt',
'thtrm_ntpf_amt',
'bsn_acti_csflw_amt',
'invsm_acti_cash_infl_amt',
'fnnr_acti_cash_infl_amt',
'cash_incre_amt',
'bsis_cash_amt',
'entrm_cash_amt',
'debt_rate',
'bsn_prft_rt_val',
'prsls_incre_rt',
'bsn_prft_incre_rt_val',
'thtrm_ntpf_incre_rt_val',
'entrp_yrmn_grrt_val',
'entrp_reltn_tdngs_dt',
'entrp_reltn_tdngs_kind_cont',
'entrp_reltn_tdngs_subjc',
'entrp_reltn_tdngs_cont_smmr',
'entrp_reltn_tdngs_dtl_cont',
'info_orgin_cont',
'entrp_reltn_tdngs_url',
'cmp_insd_reltn_info',
'cstmr_reltn_info',
'sppl_reltn_info',
'cmptt_reltn_info',
'sbst_goods_reltn_info',
'opert_sctin_cd',
'data_crtin_dt',
'cntct_prces_stts_cd',
'cntct_prces_dt'],
"표준_한글컬렴명":[
'키값',
'주식시장코드',
'현지언어주식시장명',
'영문주식시장명',
'헤브론스타국가코드',
'상장코드',
'현지언어기업명',
'영문기업명',
'해외기업법인등록번호',
'해외기업사업자등록번호',
'설립일자',
'상장일자',
'현지언어산업군명',
'영문산업군명',
'통화구분코드',
'회계연도',
'보고서종류코드',
'결산일자',
'유동자산금액',
'비유동자산금액',
'현금및예치금액',
'유가증권금액',
'대출채권금액',
'할부금융자산금액',
'리스자산금액',
'유형자산금액',
'기타자산금액',
'자산총계',
'유동부채금액',
'비유동부채금액',
'예수부채금액',
'차입부채금액',
'기타부채금액',
'부채총계',
'자본금',
'자본잉여금',
'자본조정금액',
'기타포괄손익누계액',
'이익잉여금',
'자본총계',
'부채자본총계액',
'매출액',
'매출원가금액',
'영업비용금액',
'영업이익금액',
'영업외비용금액',
'법인세비용차감전순손익금액',
'법인세비용차감전계속사업손익금액',
'법인세비용금액',
'계속사업손익법인세비용금액',
'계속사업이익금액',
'중단사업손익금액',
'당기순이익금액',
'영업활동현금흐름금액',
'투자활동현금유입금액',
'재무활동현금유입금액',
'현금증가금액',
'기초현금금액',
'기말현금금액',
'부채비율',
'영업이익율값',
'매출액증가율',
'영업이익증가율값',
'당기순이익증가율값',
'기업연평균성장률값',
'기업관련소식날짜',
'기업관련소식종류내용',
'기업관련소식제목',
'기업관련소식내용요약',
'기업관련소식상세내용',
'정보출처내용',
'기업관련소식URL',
'사내관련정보',
'고객관련정보',
'공급관련정보',
'경쟁관련정보',
'대체재관련정보',
'작업구분코드',
'데이터생성일자',
'연계처리상태코드',
'연계처리일자'
],
"데이터타입":[
'NUMERIC',
'VARCHAR(6)',
'VARCHAR(60)',
'VARCHAR(60)',
'VARCHAR(3)',
'VARCHAR(12)',
'VARCHAR(100)',
'VARCHAR(100)',
'VARCHAR(50)',
'VARCHAR(50)',
'VARCHAR(8)',
'VARCHAR(8)',
'VARCHAR(100)',
'VARCHAR(100)',
'VARCHAR(3)',
'VARCHAR(4)',
'VARCHAR(1)',
'VARCHAR(8)',
'NUMERIC',
'NUMERIC',
'NUMERIC',
'NUMERIC',
'NUMERIC',
'NUMERIC',
'NUMERIC',
'NUMERIC',
'NUMERIC',
'NUMERIC',
'NUMERIC',
'NUMERIC',
'NUMERIC',
'NUMERIC',
'NUMERIC',
'NUMERIC',
'NUMERIC',
'NUMERIC',
'NUMERIC',
'NUMERIC',
'NUMERIC',
'NUMERIC',
'NUMERIC',
'NUMERIC',
'NUMERIC',
'NUMERIC',
'NUMERIC',
'NUMERIC',
'NUMERIC',
'NUMERIC',
'NUMERIC',
'NUMERIC',
'NUMERIC',
'NUMERIC',
'NUMERIC',
'NUMERIC',
'NUMERIC',
'NUMERIC',
'NUMERIC',
'NUMERIC',
'NUMERIC',
'NUMERIC',
'VARCHAR(4)',
'NUMERIC',
'VARCHAR(4)',
'VARCHAR(4)',
'VARCHAR(4)',
'VARCHAR(8)',
'VARCHAR(10)',
'VARCHAR(100)',
'VARCHAR(1000)',
'VARCHAR(4000)',
'VARCHAR(4000)',
'VARCHAR(1000)',
'VARCHAR(4000)',
'VARCHAR(4000)',
'VARCHAR(4000)',
'VARCHAR(4000)',
'VARCHAR(4000)',
'VARCHAR(1)',
'VARCHAR(8)',
'VARCHAR(1)',
'VARCHAR(8)']
}
TableDefault = {
"한국 테이블명":[
'일본 일반 기업정보 데이터',
'홍콩 일반 기업정보 데이터',
'말레이시아 일반 기업정보 데이터',
'싱가포르 일반 기업정보 데이터',
'태국 일반 기업정보 데이터',
'베트남 일반 기업정보 데이터',
'인도네시아 일반 기업정보 데이터',
'인도 일반 기업정보 데이터',
'미국 일반 기업정보 데이터',
'캐나다 일반 기업정보 데이터',
'콜롬비아 일반 기업정보 데이터',
'멕시코 일반 기업정보 데이터',
'네덜란드 일반 기업정보 데이터',
'독일 일반 기업정보 데이터',
'이탈리아 일반 기업정보 데이터',
'프랑스 일반 기업정보 데이터',
'영국 일반 기업정보 데이터',
'호주 일반 기업정보 데이터',
'스위스 일반 기업정보 데이터',
'스페인 일반 기업정보 데이터',
'한국 상장사 재무정보 데이터',
'베트남 상장사 재무정보 데이터',
'인도네시아 상장사 재무정보 데이터',
'미국 상장사 재무정보 데이터',
'일본 상장사 재무정보 데이터',
'홍콩 상장사 재무정보 데이터',
'말레이시아 상장사 재무정보 데이터',
'싱가포르 상장사 재무정보 데이터',
'태국 상장사 재무정보 데이터',
'인도 상장사 재무정보 데이터',
'캐나다 상장사 재무정보 데이터',
'콜롬비아 상장사 재무정보 데이터',
'멕시코 상장사 재무정보 데이터',
'네덜란드 상장사 재무정보 데이터',
'독일 상장사 재무정보 데이터',
'이탈리아 상장사 재무정보 데이터',
'프랑스 상장사 재무정보 데이터',
'영국 상장사 재무정보 데이터',
'호주 상장사 재무정보 데이터',
'스위스 상장사 재무정보 데이터',
'스페인 상장사 재무정보 데이터'],
"영문 테이블명":[
'tb_hb_jpn_egnin_m',
'tb_hb_hkg_egnin_m',
'tb_hb_mys_egnin_m',
'tb_hb_sgp_egnin_m',
'tb_hb_tha_egnin_m',
'tb_hb_vnm_egnin_m',
'tb_hb_idn_egnin_m',
'tb_hb_ind_egnin_m',
'tb_hb_usa_egnin_m',
'tb_hb_can_egnin_m',
'tb_hb_col_egnin_m',
'tb_hb_mex_egnin_m',
'tb_hb_nld_egnin_m',
'tb_hb_deu_egnin_m',
'tb_hb_ita_egnin_m',
'tb_hb_fra_egnin_m',
'tb_hb_gbr_egnin_m',
'tb_hb_aus_egnin_m',
'tb_hb_che_egnin_m',
'tb_hb_esp_egnin_m',
'tb_hb_kor_plcfi_d',
'tb_hb_vnm_plcfi_d',
'tb_hb_idn_plcfi_d',
'tb_hb_usa_plcfi_d',
'tb_hb_jpn_plcfi_d',
'tb_hb_hkg_plcfi_d',
'tb_hb_mys_plcfi_d',
'tb_hb_sgp_plcfi_d',
'tb_hb_tha_plcfi_d',
'tb_hb_ind_plcfi_d',
'tb_hb_can_plcfi_d',
'tb_hb_col_plcfi_d',
'tb_hb_mex_plcfi_d',
'tb_hb_nld_plcfi_d',
'tb_hb_deu_plcfi_d',
'tb_hb_ita_plcfi_d',
'tb_hb_fra_plcfi_d',
'tb_hb_gbr_plcfi_d',
'tb_hb_aus_plcfi_d',
'tb_hb_che_plcfi_d',
'tb_hb_esp_plcfi_d']
}