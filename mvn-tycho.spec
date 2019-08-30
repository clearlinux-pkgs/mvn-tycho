#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-tycho
Version  : 1.0.0.v20140403.1907
Release  : 2
URL      : https://repo1.maven.org/maven2/org/eclipse/tycho/org.eclipse.osgi.compatibility.state/1.0.0.v20140403-1907/org.eclipse.osgi.compatibility.state-1.0.0.v20140403-1907.jar
Source0  : https://repo1.maven.org/maven2/org/eclipse/tycho/org.eclipse.osgi.compatibility.state/1.0.0.v20140403-1907/org.eclipse.osgi.compatibility.state-1.0.0.v20140403-1907.jar
Source1  : https://repo1.maven.org/maven2/org/eclipse/tycho/org.eclipse.osgi.compatibility.state/1.0.0.v20140403-1907/org.eclipse.osgi.compatibility.state-1.0.0.v20140403-1907.pom
Source2  : https://repo1.maven.org/maven2/org/eclipse/tycho/org.eclipse.osgi/3.10.0.v20140606-1445/org.eclipse.osgi-3.10.0.v20140606-1445.jar
Source3  : https://repo1.maven.org/maven2/org/eclipse/tycho/org.eclipse.osgi/3.10.0.v20140606-1445/org.eclipse.osgi-3.10.0.v20140606-1445.pom
Source4  : https://repo1.maven.org/maven2/org/eclipse/tycho/org.eclipse.tycho.core.shared/0.22.0/org.eclipse.tycho.core.shared-0.22.0.jar
Source5  : https://repo1.maven.org/maven2/org/eclipse/tycho/org.eclipse.tycho.core.shared/0.22.0/org.eclipse.tycho.core.shared-0.22.0.pom
Source6  : https://repo1.maven.org/maven2/org/eclipse/tycho/org.eclipse.tycho.embedder.shared/0.22.0/org.eclipse.tycho.embedder.shared-0.22.0.jar
Source7  : https://repo1.maven.org/maven2/org/eclipse/tycho/org.eclipse.tycho.embedder.shared/0.22.0/org.eclipse.tycho.embedder.shared-0.22.0.pom
Source8  : https://repo1.maven.org/maven2/org/eclipse/tycho/org.eclipse.tycho.p2.resolver.shared/0.22.0/org.eclipse.tycho.p2.resolver.shared-0.22.0.jar
Source9  : https://repo1.maven.org/maven2/org/eclipse/tycho/org.eclipse.tycho.p2.resolver.shared/0.22.0/org.eclipse.tycho.p2.resolver.shared-0.22.0.pom
Source10  : https://repo1.maven.org/maven2/org/eclipse/tycho/org.eclipse.tycho.p2.tools.shared/0.22.0/org.eclipse.tycho.p2.tools.shared-0.22.0.jar
Source11  : https://repo1.maven.org/maven2/org/eclipse/tycho/org.eclipse.tycho.p2.tools.shared/0.22.0/org.eclipse.tycho.p2.tools.shared-0.22.0.pom
Source12  : https://repo1.maven.org/maven2/org/eclipse/tycho/sisu-equinox-api/0.22.0/sisu-equinox-api-0.22.0.jar
Source13  : https://repo1.maven.org/maven2/org/eclipse/tycho/sisu-equinox-api/0.22.0/sisu-equinox-api-0.22.0.pom
Source14  : https://repo1.maven.org/maven2/org/eclipse/tycho/sisu-equinox-embedder/0.22.0/sisu-equinox-embedder-0.22.0.jar
Source15  : https://repo1.maven.org/maven2/org/eclipse/tycho/sisu-equinox-embedder/0.22.0/sisu-equinox-embedder-0.22.0.pom
Source16  : https://repo1.maven.org/maven2/org/eclipse/tycho/sisu-equinox/0.22.0/sisu-equinox-0.22.0.pom
Source17  : https://repo1.maven.org/maven2/org/eclipse/tycho/tycho-bundles/0.22.0/tycho-bundles-0.22.0.pom
Source18  : https://repo1.maven.org/maven2/org/eclipse/tycho/tycho-core/0.22.0/tycho-core-0.22.0.jar
Source19  : https://repo1.maven.org/maven2/org/eclipse/tycho/tycho-core/0.22.0/tycho-core-0.22.0.pom
Source20  : https://repo1.maven.org/maven2/org/eclipse/tycho/tycho-embedder-api/0.22.0/tycho-embedder-api-0.22.0.jar
Source21  : https://repo1.maven.org/maven2/org/eclipse/tycho/tycho-embedder-api/0.22.0/tycho-embedder-api-0.22.0.pom
Source22  : https://repo1.maven.org/maven2/org/eclipse/tycho/tycho-maven-plugin/0.22.0/tycho-maven-plugin-0.22.0.jar
Source23  : https://repo1.maven.org/maven2/org/eclipse/tycho/tycho-maven-plugin/0.22.0/tycho-maven-plugin-0.22.0.pom
Source24  : https://repo1.maven.org/maven2/org/eclipse/tycho/tycho-metadata-model/0.22.0/tycho-metadata-model-0.22.0.jar
Source25  : https://repo1.maven.org/maven2/org/eclipse/tycho/tycho-metadata-model/0.22.0/tycho-metadata-model-0.22.0.pom
Source26  : https://repo1.maven.org/maven2/org/eclipse/tycho/tycho-p2-facade/0.22.0/tycho-p2-facade-0.22.0.jar
Source27  : https://repo1.maven.org/maven2/org/eclipse/tycho/tycho-p2-facade/0.22.0/tycho-p2-facade-0.22.0.pom
Source28  : https://repo1.maven.org/maven2/org/eclipse/tycho/tycho-p2/0.22.0/tycho-p2-0.22.0.pom
Source29  : https://repo1.maven.org/maven2/org/eclipse/tycho/tycho/0.22.0/tycho-0.22.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : EPL-1.0
Requires: mvn-tycho-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-tycho package.
Group: Data

%description data
data components for the mvn-tycho package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/org.eclipse.osgi.compatibility.state/1.0.0.v20140403-1907
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/org.eclipse.osgi.compatibility.state/1.0.0.v20140403-1907

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/org.eclipse.osgi.compatibility.state/1.0.0.v20140403-1907
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/org.eclipse.osgi.compatibility.state/1.0.0.v20140403-1907

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/org.eclipse.osgi/3.10.0.v20140606-1445
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/org.eclipse.osgi/3.10.0.v20140606-1445

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/org.eclipse.osgi/3.10.0.v20140606-1445
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/org.eclipse.osgi/3.10.0.v20140606-1445

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/org.eclipse.tycho.core.shared/0.22.0
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/org.eclipse.tycho.core.shared/0.22.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/org.eclipse.tycho.core.shared/0.22.0
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/org.eclipse.tycho.core.shared/0.22.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/org.eclipse.tycho.embedder.shared/0.22.0
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/org.eclipse.tycho.embedder.shared/0.22.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/org.eclipse.tycho.embedder.shared/0.22.0
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/org.eclipse.tycho.embedder.shared/0.22.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/org.eclipse.tycho.p2.resolver.shared/0.22.0
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/org.eclipse.tycho.p2.resolver.shared/0.22.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/org.eclipse.tycho.p2.resolver.shared/0.22.0
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/org.eclipse.tycho.p2.resolver.shared/0.22.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/org.eclipse.tycho.p2.tools.shared/0.22.0
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/org.eclipse.tycho.p2.tools.shared/0.22.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/org.eclipse.tycho.p2.tools.shared/0.22.0
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/org.eclipse.tycho.p2.tools.shared/0.22.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/sisu-equinox-api/0.22.0
cp %{SOURCE12} %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/sisu-equinox-api/0.22.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/sisu-equinox-api/0.22.0
cp %{SOURCE13} %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/sisu-equinox-api/0.22.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/sisu-equinox-embedder/0.22.0
cp %{SOURCE14} %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/sisu-equinox-embedder/0.22.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/sisu-equinox-embedder/0.22.0
cp %{SOURCE15} %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/sisu-equinox-embedder/0.22.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/sisu-equinox/0.22.0
cp %{SOURCE16} %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/sisu-equinox/0.22.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/tycho-bundles/0.22.0
cp %{SOURCE17} %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/tycho-bundles/0.22.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/tycho-core/0.22.0
cp %{SOURCE18} %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/tycho-core/0.22.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/tycho-core/0.22.0
cp %{SOURCE19} %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/tycho-core/0.22.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/tycho-embedder-api/0.22.0
cp %{SOURCE20} %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/tycho-embedder-api/0.22.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/tycho-embedder-api/0.22.0
cp %{SOURCE21} %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/tycho-embedder-api/0.22.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/tycho-maven-plugin/0.22.0
cp %{SOURCE22} %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/tycho-maven-plugin/0.22.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/tycho-maven-plugin/0.22.0
cp %{SOURCE23} %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/tycho-maven-plugin/0.22.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/tycho-metadata-model/0.22.0
cp %{SOURCE24} %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/tycho-metadata-model/0.22.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/tycho-metadata-model/0.22.0
cp %{SOURCE25} %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/tycho-metadata-model/0.22.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/tycho-p2-facade/0.22.0
cp %{SOURCE26} %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/tycho-p2-facade/0.22.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/tycho-p2-facade/0.22.0
cp %{SOURCE27} %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/tycho-p2-facade/0.22.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/tycho-p2/0.22.0
cp %{SOURCE28} %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/tycho-p2/0.22.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/tycho/0.22.0
cp %{SOURCE29} %{buildroot}/usr/share/java/.m2/repository/org/eclipse/tycho/tycho/0.22.0


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/eclipse/tycho/org.eclipse.osgi.compatibility.state/1.0.0.v20140403-1907/org.eclipse.osgi.compatibility.state-1.0.0.v20140403-1907.jar
/usr/share/java/.m2/repository/org/eclipse/tycho/org.eclipse.osgi.compatibility.state/1.0.0.v20140403-1907/org.eclipse.osgi.compatibility.state-1.0.0.v20140403-1907.pom
/usr/share/java/.m2/repository/org/eclipse/tycho/org.eclipse.osgi/3.10.0.v20140606-1445/org.eclipse.osgi-3.10.0.v20140606-1445.jar
/usr/share/java/.m2/repository/org/eclipse/tycho/org.eclipse.osgi/3.10.0.v20140606-1445/org.eclipse.osgi-3.10.0.v20140606-1445.pom
/usr/share/java/.m2/repository/org/eclipse/tycho/org.eclipse.tycho.core.shared/0.22.0/org.eclipse.tycho.core.shared-0.22.0.jar
/usr/share/java/.m2/repository/org/eclipse/tycho/org.eclipse.tycho.core.shared/0.22.0/org.eclipse.tycho.core.shared-0.22.0.pom
/usr/share/java/.m2/repository/org/eclipse/tycho/org.eclipse.tycho.embedder.shared/0.22.0/org.eclipse.tycho.embedder.shared-0.22.0.jar
/usr/share/java/.m2/repository/org/eclipse/tycho/org.eclipse.tycho.embedder.shared/0.22.0/org.eclipse.tycho.embedder.shared-0.22.0.pom
/usr/share/java/.m2/repository/org/eclipse/tycho/org.eclipse.tycho.p2.resolver.shared/0.22.0/org.eclipse.tycho.p2.resolver.shared-0.22.0.jar
/usr/share/java/.m2/repository/org/eclipse/tycho/org.eclipse.tycho.p2.resolver.shared/0.22.0/org.eclipse.tycho.p2.resolver.shared-0.22.0.pom
/usr/share/java/.m2/repository/org/eclipse/tycho/org.eclipse.tycho.p2.tools.shared/0.22.0/org.eclipse.tycho.p2.tools.shared-0.22.0.jar
/usr/share/java/.m2/repository/org/eclipse/tycho/org.eclipse.tycho.p2.tools.shared/0.22.0/org.eclipse.tycho.p2.tools.shared-0.22.0.pom
/usr/share/java/.m2/repository/org/eclipse/tycho/sisu-equinox-api/0.22.0/sisu-equinox-api-0.22.0.jar
/usr/share/java/.m2/repository/org/eclipse/tycho/sisu-equinox-api/0.22.0/sisu-equinox-api-0.22.0.pom
/usr/share/java/.m2/repository/org/eclipse/tycho/sisu-equinox-embedder/0.22.0/sisu-equinox-embedder-0.22.0.jar
/usr/share/java/.m2/repository/org/eclipse/tycho/sisu-equinox-embedder/0.22.0/sisu-equinox-embedder-0.22.0.pom
/usr/share/java/.m2/repository/org/eclipse/tycho/sisu-equinox/0.22.0/sisu-equinox-0.22.0.pom
/usr/share/java/.m2/repository/org/eclipse/tycho/tycho-bundles/0.22.0/tycho-bundles-0.22.0.pom
/usr/share/java/.m2/repository/org/eclipse/tycho/tycho-core/0.22.0/tycho-core-0.22.0.jar
/usr/share/java/.m2/repository/org/eclipse/tycho/tycho-core/0.22.0/tycho-core-0.22.0.pom
/usr/share/java/.m2/repository/org/eclipse/tycho/tycho-embedder-api/0.22.0/tycho-embedder-api-0.22.0.jar
/usr/share/java/.m2/repository/org/eclipse/tycho/tycho-embedder-api/0.22.0/tycho-embedder-api-0.22.0.pom
/usr/share/java/.m2/repository/org/eclipse/tycho/tycho-maven-plugin/0.22.0/tycho-maven-plugin-0.22.0.jar
/usr/share/java/.m2/repository/org/eclipse/tycho/tycho-maven-plugin/0.22.0/tycho-maven-plugin-0.22.0.pom
/usr/share/java/.m2/repository/org/eclipse/tycho/tycho-metadata-model/0.22.0/tycho-metadata-model-0.22.0.jar
/usr/share/java/.m2/repository/org/eclipse/tycho/tycho-metadata-model/0.22.0/tycho-metadata-model-0.22.0.pom
/usr/share/java/.m2/repository/org/eclipse/tycho/tycho-p2-facade/0.22.0/tycho-p2-facade-0.22.0.jar
/usr/share/java/.m2/repository/org/eclipse/tycho/tycho-p2-facade/0.22.0/tycho-p2-facade-0.22.0.pom
/usr/share/java/.m2/repository/org/eclipse/tycho/tycho-p2/0.22.0/tycho-p2-0.22.0.pom
/usr/share/java/.m2/repository/org/eclipse/tycho/tycho/0.22.0/tycho-0.22.0.pom
