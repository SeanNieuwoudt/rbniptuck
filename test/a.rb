Role.create([
  {:name => :super_admin,               :group => :platform},
  {:name => :management,                :group => :platform},
  {:name => :brand_marketing,           :group => :platform},
  {:name => :auditor,                   :group => :platform},
  {:name => :support_agent,             :group => :platform},
  {:name => :senior_bank_management,    :group => :bank},
  {:name => :business_consumer_banking, :group => :bank},
  {:name => :bank_support_agent,        :group => :bank},
  {:name => :bank_auditor,              :group => :bank},
  {:name => :merchant_management,       :group => :merchant},
  {:name => :merchant_marketing,        :group => :merchant}
])